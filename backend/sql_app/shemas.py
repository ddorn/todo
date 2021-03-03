from datetime import date
from typing import List, Optional

from pydantic import BaseModel


# -------- Todos --------- #

class TodoCreate(BaseModel):
    name: str
    categ: str


class Todo(BaseModel):
    name: str
    categ: str
    id: int
    done: bool
    important: bool
    deadline: Optional[date]

    class Config:
        orm_mode = True


class PartialTodo(BaseModel):
    name: Optional[str]
    categ: Optional[str]
    done: Optional[bool]
    important: Optional[bool]
    deadline: Optional[date]


# -------- TodoLists --------- #

class TodoListCreate(BaseModel):
    title: str
    description: Optional[str] = ""


class TodoList(BaseModel):
    id: int
    title: str
    description: Optional[str] = ""
    todos: List[Todo] = []

    class Config:
        orm_mode = True


class TodoListMetaData(BaseModel):
    id: int
    title: str
    description: Optional[str] = ""

    class Config:
        orm_mode = True
