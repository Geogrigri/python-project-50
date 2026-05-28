import json
from pathlib import Path

import yaml


def parse_file(filepath):
    extension = Path(filepath).suffix

    with open(filepath) as file:
        if extension == ".json":
            return json.load(file)

        if extension in (".yml", ".yaml"):
            return yaml.safe_load(file)

    raise ValueError(f"Unsupported file format: {extension}")
