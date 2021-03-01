import os
from pathlib import Path

__all__ = ["TOP_DIR", "DATA", "CONFIG_FILE", "DB_FILE", "SQLALCHEMY_DATABASE_URL", "DEV"]

TOP_DIR = Path(__file__).parent
DATA = TOP_DIR / "data"
CONFIG_FILE = DATA / 'config.json'
DB_FILE = DATA / 'todo.db'
SQLALCHEMY_DATABASE_URL = "sqlite:///" + str(DB_FILE)
DEV = os.environ.get('DEV', False)
