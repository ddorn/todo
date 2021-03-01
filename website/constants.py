import os
from pathlib import Path

TOP_DIR = Path(__file__).parent
DATA = TOP_DIR / "data"
CONFIG_FILE = DATA / 'config.json'
TODO_FILE = DATA / 'todos.yaml'
DB_FILE = DATA / 'todo.db'
SQLALCHEMY_DATABASE_URL = "sqlite:///" + str(DB_FILE)
DEV = os.environ.get('DEV', False)

del Path, os
