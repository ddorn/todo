import os
import json
import random
from operator import attrgetter, itemgetter
from pathlib import Path
from typing import Dict, List
import yaml

TOP_DIR = Path(__file__).parent
DATA = TOP_DIR / "data"
CONFIG_FILE = DATA / 'config.json'
TODO_FILE = DATA / 'todos.yaml'

os.chdir(TOP_DIR)

def get_config(key):
    return json.loads(CONFIG_FILE.read_text())[key]


def load_todos() -> Dict[int, Dict]:
    TODO_FILE.touch()
    return yaml.safe_load(TODO_FILE.read_text() or '{}')


def save_todos(todos):
    assert isinstance(todos, dict)
    TODO_FILE.write_text(yaml.safe_dump(todos))


def get(l, **kwargs):
    getters = [
        (attrgetter(key) if key[0] != '_' else itemgetter(key[1:]), value)
        for key, value in kwargs.items()
    ]
    for el in l:
        if all(getter(el) == value for getter, value in getters):
            return el
    return None

if __name__ == '__main__':
    pass
