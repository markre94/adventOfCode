from pathlib import Path


def load_input(path: Path = None) -> str:
    if not path:
        path = Path.cwd() / "input.txt"

    return path.read_text()
