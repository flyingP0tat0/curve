#!/bin/sh

pip3 install requirements.txt \
  || pip install requirements.txt \
  || echo "No pip found."
