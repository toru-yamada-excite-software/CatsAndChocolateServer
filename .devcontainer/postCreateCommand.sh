#!/bin/sh

echo "START Install"

poetry config virtualenvs.in-project true
poetry install

echo "FINISH Install"