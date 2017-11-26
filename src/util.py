import os
import yaml

def get_config(file):
  try:
    with open(os.path.dirname(__file__) + "/../config/" + file, "r") as yml:
      config = yaml.load(yml)

  except FileNotFoundError:
    with open(os.path.dirname(__file__) + "/" + file, "r") as yml:
      config = yaml.load(yml)

  return config
