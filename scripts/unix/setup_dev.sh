#!/bin/sh

pip3 install requirements_dev.txt \
  || pip install requirements_dev.txt \
  || echo "No pip found."
