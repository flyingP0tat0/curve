#!/bin/sh

python3 src/main.py \
  || python src/main.py \
  || echo "No python found."
