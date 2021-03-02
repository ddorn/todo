from typing import Optional

from sqlalchemy.orm import Session

from . import models, shemas


def get_todo(db: Session, id: int) -> models.Todo:
    return db.query(models.Todo).filter(models.Todo.id == id).first()


def create_todo(db: Session, todo: shemas.TodoCreate, list_id) -> Optional[models.Todo]:
    db_todo = models.Todo(**todo.dict(), list_id=list_id)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo


def update_todo(db: Session, todo_id: int, modif: shemas.PartialTodo) -> Optional[models.Todo]:
    db_todo = get_todo(db, todo_id)
    if db_todo is None:
        return None
    for k, v in modif.dict(exclude_unset=True).items():
        setattr(db_todo, k, v)
    db.commit()
    db.refresh(db_todo)  # Should be useless
    return db_todo


def delete_todo(db: Session, todo_id: int) -> models.Todo:
    todo = get_todo(db, todo_id)
    if todo is not None:
        db.delete(todo)
    return todo


def create_list(db: Session, list: shemas.TodoListCreate) -> models.TodoList:
    db_list = models.TodoList(**list.dict())
    db.add(db_list)
    db.commit()
    db.refresh(db_list)
    return db_list


def get_list(db: Session, id: int) -> models.TodoList:
    return db.query(models.TodoList).filter(models.TodoList.id == id).first()


def get_all_lists(db: Session):
    return db.query(models.TodoList).all()
