#!/usr/bin/env bash

export QDRANT_URL=$1
export TS_PROJECT_PATH=$2

SCRIPT_PATH="$( cd "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"
ROOT_PATH=$SCRIPT_PATH/..

python3 -m venv .venv
source .venv/bin/activate
pip install -r code_search/index_ts/requirements_snippets.txt
python3 -m code_search.index_ts.create_qdrant_snippets
python3 -m code_search.index_ts.files_to_json
cat <<EOF > $ROOT_PATH/tools/ts_send_snippets.sh
#!/bin/bash
cd /app
python3 -m venv .dvenv
source .dvenv/bin/activate
pip install -r requirements.txt
python3 -m code_search.index_ts.upload_code
python3 -m code_search.index_ts.upload_signatures
python3 -m code_search.index_ts.file_uploader
EOF

docker run --rm -e "QDRANT_URL=$QDRANT_URL" -v $ROOT_PATH:/app python:3.11 /bin/bash -c "source /app/tools/ts_send_snippets.sh"