import os
from pathlib import Path

__all__ = ["BACKEND_DIR", "DATA", "CONFIG_FILE", "DB_FILE", "SQLALCHEMY_DATABASE_URL", "DEV", "FRONTEND_DIR", "FRONTEND_BUILD"]

BACKEND_DIR = Path(__file__).parent
FRONTEND_DIR = BACKEND_DIR.parent / "frontend"
DATA = BACKEND_DIR / "data"
CONFIG_FILE = DATA / 'config.json'
DB_FILE = DATA / 'todo.db'
SQLALCHEMY_DATABASE_URL = "sqlite:///" + str(DB_FILE)
DEV = os.environ.get('DEV', False)
FRONTEND_BUILD = FRONTEND_DIR / "dist"
