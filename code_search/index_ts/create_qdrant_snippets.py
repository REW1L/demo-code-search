import docker
import json
import os
import re
from pathlib import Path

from code_search.index_ts import scip_pb2, files_to_json
from code_search.config import DATA_DIR

class QdrantSnippet:
  file: str
  symbol: str
  module: str
  name: str
  start_line: str
  start_character: str
  end_line: str
  end_character: str
  code_snippet: str
  code_type: str
  signature: str
  docstring: str
  def get_snippet(self):
    return {
      "file": self.file,
      "start_line": self.start_line,
      "start_character": self.start_character,
      "end_line": self.end_line,
      "end_character": self.end_character,
      "code_snippet": self.code_snippet,
    }
  def get_structure(self):
    return {
        "name": self.name,
        "signature": self.signature,
        "code_type": self.code_type,
        "docstring": self.docstring,
        "line": self.start_line,
        "line_from": self.start_line,
        "line_to": self.end_line,
        "context": {
            "module": self.module,
            "file_path": self.file,
            "file_name": Path(self.file).name,
            "struct_name": self.name[:self.name.find("#")],
            "snippet": self.code_snippet
        }
    }

class ScipTypescript:
  def __init__(self, project_path: str | Path):
    self.project_path = Path.absolute(Path(project_path))
    self.index = scip_pb2.Index()

  def create_index(self, overwrite: bool = False, output_path: str | Path = "./out_index/"):
    client = docker.from_env()
    output_path = Path.absolute(Path(output_path))
    if not output_path.exists():
      os.makedirs(output_path)
    if not Path(f"{output_path}/index.scip").exists() or overwrite:
      client.containers.run(
        "node:22",
        volumes={
          str(self.project_path): {"bind": str(self.project_path), "mode": "ro"},
          str(output_path): {"bind": "/out", "mode": "rw"}
          },
        entrypoint=["/usr/local/bin/npx"],
        command=[
          "-y",
          "@sourcegraph/scip-typescript", "index",
          "--cwd", str(self.project_path),
          "--output", "/out/index.scip",
          ],
        detach=False,
        remove=True
      )
    with open(f"{output_path}/index.scip", "rb") as f:
      self.index.ParseFromString(f.read())

  def get_snippets(self):
    snippets = []
    for doc in self.index.documents:
      symbols = {}
      for symbol_info in doc.symbols:
        symbols[symbol_info.symbol] = symbol_info
      doc_lines = Path(f"{self.project_path}/{doc.relative_path}").read_text().split("\n")
      for occurrence in doc.occurrences:
        # we are interested only in defined code blocks (functions and classes)
        if occurrence.enclosing_range:
          code_range = occurrence.enclosing_range
        else:
          continue
        if not occurrence.symbol[occurrence.symbol.rfind("/")+1:]:
          continue
        if occurrence.symbol not in symbols:
          continue
        if symbols[occurrence.symbol].documentation and (
            symbols[occurrence.symbol].documentation[0].startswith("```ts\n(parameter) ")
            or symbols[occurrence.symbol].documentation[0].startswith("```ts\nvar ")
            or symbols[occurrence.symbol].documentation[0].startswith("```ts\n(property) ")
          ):
          continue

        qdrant_snippet = QdrantSnippet()
        symbol_parts = occurrence.symbol.split(" ")
        qdrant_snippet.module = symbol_parts[2]
        qdrant_snippet.symbol = symbol_parts[-1]
        qdrant_snippet.name = qdrant_snippet.symbol[qdrant_snippet.symbol.rfind("/")+1:-1]
        qdrant_snippet.file = doc.relative_path
        start_line = code_range[0]
        qdrant_snippet.start_line = start_line
        qdrant_snippet.start_character = code_range[1]
        if len(code_range) == 4:
          end_line = code_range[2]
          qdrant_snippet.end_character = code_range[3]
        else:
          end_line = start_line
          qdrant_snippet.end_character = code_range[2]
        qdrant_snippet.end_line = end_line
        # enclosing_range is a half-open [start, end) range of this occurrence
        qdrant_snippet.code_snippet = "\n".join(doc_lines[start_line : end_line + 1].copy())
        code_type = re.match(r"^```ts\n((\(|[a-zA-Z])[^ \(]+).*", symbols[occurrence.symbol].documentation[0])
        if code_type is not None:
          qdrant_snippet.code_type = code_type.group(1).strip("()")
        else:
          qdrant_snippet.code_type = "undefined"
        # removing ```ts\n...\n``` from signature
        qdrant_snippet.signature = symbols[occurrence.symbol].documentation[0][6:-4]
        qdrant_snippet.docstring = "\n".join(symbols[occurrence.symbol].documentation[1:])
        snippets.append(qdrant_snippet)
    return snippets

def main():
  TS_PROJECT_PATH = os.getenv("TS_PROJECT_PATH")
  scip = ScipTypescript(TS_PROJECT_PATH)
  scip.create_index(True)
  entries = scip.get_snippets()
  with open(Path(DATA_DIR) / "qdrant_snippets.jsonl", "w") as snippets_fp:
    with open(Path(DATA_DIR) / "structures.json", "w") as structures_fp:
      for entry in entries:
        entry: QdrantSnippet
        snippets_fp.write(json.dumps(entry.get_snippet()) + "\n")
        if entry.code_type in ["class", "interface"]:
          structures_fp.write(json.dumps(entry.get_structure()) + "\n")

  files_data = files_to_json.explore_directory(TS_PROJECT_PATH)
  with open(Path(DATA_DIR) / "ts_files.json", 'w', encoding='utf-8') as json_file:
    json.dump(files_data, json_file, indent=2)

if __name__ == "__main__":
  main()
