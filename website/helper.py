import yaml

import crud
import shemas
from constants import *
from database import SessionLocal


def load_todos():
    TODO_FILE.touch()
    data = yaml.safe_load(TODO_FILE.read_text() or '{}')
    return data


if __name__ == '__main__':
    db = SessionLocal()

    for todo in load_todos().values():
        crud.create_todo(db, shemas.TodoCreate(name=todo['name'], categ=todo['categ']), 1)
