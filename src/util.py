import os
import yaml

dir = os.path.dirname(__file__)

def get_root():
    if os.path.isdir(os.path.join(dir, "config")):
        return dir
    else:
        return os.path.join(dir, "..")

def get_config(file):
    root = get_root()
    with open(os.path.join(root, "config/" + file), "r") as yml:
        config = yaml.load(yml)

    return config
