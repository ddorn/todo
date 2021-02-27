from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


__all__ = ["Todo", "TodoList"]


class Todo(Base):
    __tablename__ = 'todos'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    categ = Column(String, index=True)
    done = Column(Boolean, default=False)
    important = Column(Boolean, default=False)

    list_id = Column(Integer, ForeignKey("todolists.id"))
    list = relationship("TodoList", back_populates='todos')


class TodoList(Base):
    __tablename__ = 'todolists'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)

    todos = relationship("Todo", back_populates='list')
