#!/bin/sh

pip3 install -r requirements_dev.txt \
  || pip install -r requirements_dev.txt \
  || echo "No pip found."
