from typing import Annotated
from alembic.util import status
from fastapi import APIRouter, Depends, status, Path,HTTPException
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from typing import Annotated
from models import Base, Todo
from database import engine, SessionLocal

router = APIRouter(
    prefix="/todos",
    tags=["Todo"],
)

Base.metadata.create_all(bind=engine)


class TodoRequest(BaseModel):
    title : str = Field(min_length=3,max_length=100)
    description :str = Field(min_length=3,max_length=100)
    priority: int = Field(gt=0)
    complete: bool


def get_db():
    db = SessionLocal()
    try:
        yield db #like return = yield
        #yield can return more than one values
    finally:
        db.close()

db_dependency = Annotated[Session,Depends(get_db)]

@router.get("/read_all")
async def read_all(db: db_dependency):
    return db.query(Todo).all()

@router.get("/get_by_id/{todo_id}",status_code=status.HTTP_200_OK)
async def read_by_id(db: db_dependency,todo_id: int = Path(gt=0)):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if todo is not None:
        return todo
    raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,detail = "Todo Not Found!")



@router.post("/create",status_code=status.HTTP_201_CREATED)
async def create_todo(db: db_dependency,todo_request: TodoRequest):
    todo = Todo(**todo_request.dict())
    db.add(todo)
    db.commit() # dont forget

@router.put("/update/{todo_id}")
async def update_todo(db:db_dependency, todo_request:TodoRequest, todo_id:int = Path(gt=0)):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if todo is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Todo is not found!")

    todo.title = todo_request.title
    todo.description = todo_request.description
    todo.priority = todo_request.priority
    todo.complete = todo_request.complete

    db.add(todo)
    db.commit()

@router.delete("/delete/{todo_id}",status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(db:db_dependency,todo_id:int = Path(gt=0)):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if todo is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Todo is not found!")
    #db.query(Todo).filter(Todo.id == todo_id).first()
    #for ensure to delete correct data
    db.delete(todo)
    db.commit()



