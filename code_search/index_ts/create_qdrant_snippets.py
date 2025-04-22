import os.path
from pathlib import Path
import docker
import json
import os
import re
from pathlib import Path

from code_search.index_ts import scip_pb2
from code_search.config import DATA_DIR


class QdrantSnippet:
  file: str
  start_line: str
  start_character: str
  end_line: str
  end_character: str
  code_snippet: str
  def __dict__(self):
    return {
      "file": self.file,
      "start_line": self.start_line,
      "start_character": self.start_character,
      "end_line": self.end_line,
      "end_character": self.end_character,
      "code_snippet": self.code_snippet
    }

class QdrantSignatureStructure:
  class Context:
    module: str = ""
    file_path: str = ""
    file_name: str = ""
    struct_name: str = ""
    snippet: str = ""
  name: str = ""
  signature: str = ""
  code_type: str = ""
  docstring: str = ""
  line: int = 0
  line_from: int = 0
  line_to: int = 0
  context: Context
  def __dict__(self):
    return {
        "name": self.name,
        "signature": self.signature,
        "code_type": self.code_type,
        "docstring": self.docstring,
        "line": self.line,
        "line_from": self.line_from,
        "line_to": self.line_to,
        "context": {
            "module": self.context.module,
            "file_path": self.context.file_path,
            "file_name": self.context.file_name,
            "struct_name": self.context.struct_name,
            "snippet": self.context.snippet
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
      doc_lines = Path(f"{self.project_path}/{doc.relative_path}").read_text().split("\n")
      for occurrence in doc.occurrences:
        qdrant_snippet = QdrantSnippet()
        qdrant_snippet.file = doc.relative_path
        code_range = occurrence.enclosing_range if occurrence.enclosing_range else occurrence.range
        start_line = code_range[0]
        qdrant_snippet.start_line = start_line
        qdrant_snippet.start_character = code_range[1]
        if len(code_range) == 4:
          end_line = code_range[2]
          qdrant_snippet.end_character = code_range[3]
        else:
          end_line = code_range[0]
          qdrant_snippet.end_character = code_range[2]
        qdrant_snippet.end_line = end_line
        code_snippet = "\n".join(doc_lines[start_line : end_line + 1])
        if not code_snippet.startswith("import"):
          qdrant_snippet.code_snippet = code_snippet
          snippets.append(qdrant_snippet.__dict__())
    return snippets

  def get_signatures(self):
    signatures = []
    for doc in self.index.documents:
      symbols = {}
      for symbol_info in doc.symbols:
        symbols[symbol_info.symbol] = symbol_info
      doc_lines = Path(f"{self.project_path}/{doc.relative_path}").read_text().split("\n")
      for occurrence in doc.occurrences:
        symbol_info = symbols.get(occurrence.symbol)
        if symbol_info is None:
          continue
        signature = QdrantSignatureStructure()
        signature.context = QdrantSignatureStructure.Context()
        signature.context.file_name = Path(doc.relative_path).name
        signature.context.file_path = doc.relative_path
        descriptor = "(" \
                     "(?P<namespace>.+\/)|" \
                     "(?P<type>.+#)|" \
                     "(?P<term>.+\.)|" \
                     "(?P<meta>.+:)|" \
                     "(?P<macro>.+!)|" \
                     "(?P<method>.+\(.*\))|" \
                     "(?P<parameter>\(.*\))|" \
                     "(?P<type_parameter>\[.*\])" \
                     ")"
        symbol_parts = re.match(
          "^(?P<scheme>[^ ]+) "
          "(?P<package_manager>[^ ]+) (?P<package_name>[^ ]+) (?P<package_version>[^ ]+) "
          f"{descriptor}+",
          occurrence.symbol
        )
        if symbol_parts is None:
          continue
        signature_parsed = symbol_parts.groupdict()
        signature.name = symbol_parts.group(5)
        function = re.match(r"^```ts\n(?P<signature>[a-zA-Z0-9_]+\(.*\).*)\n```$", symbol_info.documentation[0])
        code = re.match(r"^```ts\n(?P<type>[^ ]+) (?P<signature>[^\n]+)\n```$", symbol_info.documentation[0])
        if function is not None:
          signature.code_type = "function"
          signature.signature = function.group("signature")
        elif code is not None:
          signature.code_type = code.group("type")
          signature.signature = code.group("signature")
        signature.docstring = "\n".join(symbol_info.documentation[1:])
        signature.context.module = signature_parsed.get("package_name", "")
        signature.context.struct_name = signature_parsed.get("type", "")
        signature.line = occurrence.range[0]
        code_range = occurrence.enclosing_range if occurrence.enclosing_range else occurrence.range
        signature.line = code_range[0]
        signature.line_from = code_range[0]
        if len(code_range) == 4:
          signature.line_to = code_range[2]
        else:
          signature.line_to = code_range[0]
        signature.context.snippet = "\n".join(doc_lines[signature.line_from : signature.line_to + 1])
        signatures.append(signature.__dict__())
    return signatures

def main():
  TS_PROJECT_PATH = os.getenv("TS_PROJECT_PATH")
  scip = ScipTypescript(TS_PROJECT_PATH)
  scip.create_index()
  entries = scip.get_snippets()
  with open(Path(DATA_DIR) / "qdrant_snippets.jsonl", "w") as fp:
    for entry in entries:
      fp.write(json.dumps(entry) + "\n")
  signatures = scip.get_signatures()
  with open(Path(DATA_DIR) / "structures.json", "w") as fp:
    for entry in signatures:
      fp.write(json.dumps(entry) + "\n")


if __name__ == "__main__":
  main()
