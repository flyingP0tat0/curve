#!/bin/sh

python3 -m unittest discover -s test -p "*_test.py" \
  || python -m unittest discover -s test -p "*_test.py" \
  || echo "No python found."
