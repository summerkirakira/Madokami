import toml
from pathlib import Path

file_path = Path(__file__).parent / 'pyproject.toml'


def get_version():
    with open(file_path, 'r') as f:
        data = toml.load(f)
    return data['tool']['poetry']['version']


if __name__ == "__main__":
    version = get_version()
    print(version)
