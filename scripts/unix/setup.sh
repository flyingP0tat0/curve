#!/bin/sh

pip3 install -r requirements.txt \
  || pip install -r requirements.txt \
  || echo "No pip found."
