import os
import yaml

def get_config(file):
    with open(os.path.dirname(__file__) + "/../config/" + file, "r") as yml:
        config = yaml.load(yml)

    return config
