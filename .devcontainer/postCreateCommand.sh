#!/bin/sh

echo "START Install"

sudo chown -R vscode:vscode .venv
poetry config virtualenvs.in-project true
poetry install

echo "FINISH Install"