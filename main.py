"""
"""
from typing import Dict, Optional
from fastapi import FastAPI, HTTPException, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from starlette.responses import HTMLResponse

from helper import *

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


def template(name, request, **kwargs):
    return templates.TemplateResponse(name, {
        'request': request,
        **kwargs
    })


# ####################### User pages ####################### #

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return template('home.html', request, title="Liste de courses")


# ####################### API ####################### #

class Todo(BaseModel):
    name: str
    categ: str
    done: bool
    id: Optional[int] = 0


class PartialTodo(BaseModel):
    name: Optional[str]
    categ: Optional[str]
    done: Optional[bool]


@app.get("/api")
def get_all_todos():
    """Get all the todos."""
    return list(load_todos().values())


@app.post("/api", response_model=Todo)
def create_new_todo(todo: Todo):
    """Create a new to-do. The system ID is in the response."""
    todos = load_todos()
    new_id = max(todos, default=-1) + 1
    todo.id = new_id
    todos[new_id] = todo.dict()

    save_todos(todos)

    return todo


@app.get("/api/todo/{id}", response_model=Todo)
def get_single_todo(id: int):
    todos = load_todos()
    if id not in todos:
        return HTTPException(404, "Todo not found")
    return todos[id]


@app.patch("/api/todo/{id}", response_model=Todo)
def update_todo(id: int, todo: PartialTodo):
    """Modify an existing to-do."""
    todos = load_todos()
    if id not in todos:
        return HTTPException(404, "Todo not found")

    saved_todo = todos[id]
    new_values = todo.dict(exclude_unset=True)
    saved_todo.update(**new_values)

    save_todos(todos)
    return saved_todo


@app.delete("/api/todo/{id}")
def delete_todo(id: int):
    """Delete an existing to-do."""
    todos = load_todos()
    if id not in todos:
        return HTTPException(404, "Todo not found")

    del todos[id]
