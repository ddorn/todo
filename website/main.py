"""
"""
import os
from typing import List

from fastapi import APIRouter, FastAPI, HTTPException, Request, Depends
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from starlette.responses import HTMLResponse

from sql_app import crud, models, shemas
from constants import *
from sql_app.database import engine, get_db

os.chdir(TOP_DIR)

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


def template(name, request, **kwargs):
    return templates.TemplateResponse(name, {
        'request': request,
        **kwargs
    })


# ####################### User pages ####################### #

@app.get("/", response_class=HTMLResponse, tags=['Webpages'])
def home(request: Request):
    return template('home.html', request, title="Listes de Diego", DEV=DEV)


# ####################### API ####################### #

list_router = APIRouter(prefix='/list', tags=['Todo Lists'])

@list_router.get("/", response_model=List[shemas.TodoListMetaData])
def get_all_todolists(db = Depends(get_db)):
    return crud.get_all_lists(db)

@list_router.post("/", response_model=shemas.TodoList)
def create_todolist(list: shemas.TodoListCreate, db = Depends(get_db)):
    return crud.create_list(db, list)


@list_router.get("/{id}", response_model=List[shemas.Todo])
def get_all_todos(id: int, db: Session = Depends(get_db)):
    """Get all the todos in the list."""
    db_list = crud.get_list(db, id)
    if db_list is None:
        return []
    return db_list.todos


@list_router.post("/{id}", response_model=shemas.Todo)
def create_todo(id: int, todo: shemas.TodoCreate, db = Depends(get_db)):
    return crud.create_todo(db, todo, id)


todo_router = APIRouter(prefix="/todo",
                        tags=['Todos'])

@todo_router.get("/{id}", response_model=shemas.Todo)
def get_single_todo(id: int, db: Session = Depends(get_db)):
    db_todo = crud.get_todo(db, id)
    if db_todo is None:
        raise HTTPException(404, "Todo not found")
    return db_todo


@todo_router.patch("/{id}", response_model=shemas.Todo)
def update_todo(id: int, todo: shemas.PartialTodo, db: Session = Depends(get_db)):
    """Modify an existing to-do."""
    updated = crud.update_todo(db, id, todo)
    if updated is None:
        raise HTTPException(404, "Todo not found")
    return updated


@todo_router.delete("/{id}")
def delete_todo(id: int, db: Session = Depends(get_db)):
    """Delete an existing to-do."""
    if not crud.delete_todo(db, id):
        return HTTPException(404, "Todo not found")

api = APIRouter(prefix='/api')
api.include_router(list_router)
api.include_router(todo_router)
app.include_router(api)
