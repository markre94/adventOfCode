import json
from pathlib import Path


def load_input(path: Path = None) -> str:
    if not path:
        path = Path.cwd() / "input.txt"

    return path.read_text()


def load_input_as_json(path: Path = None) -> dict:
    if not path:
        path = Path.cwd() / "input.txt"

    with open(path) as file:
        s = file.read()
        return json.loads(s)
