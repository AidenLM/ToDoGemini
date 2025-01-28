from typing import Annotated
from alembic.util import status
from fastapi import APIRouter, Depends, status, Path,HTTPException,Request
from langchain.retrievers.document_compressors.chain_filter import default_get_input
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from typing import Annotated
from starlette.responses import RedirectResponse

from models import Base, Todo
from database import engine, SessionLocal
from routers.auth import get_current_user
from fastapi.templating import Jinja2Templates

router = APIRouter(
    prefix="/todo",
    tags=["Todo"],
)

templates = Jinja2Templates(directory="templates")

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
user_dependency = Annotated[dict,Depends(get_current_user)]

def redirect_to_login():
    redirect_response = RedirectResponse(url="/auth/login-page",status_code=status.HTTP_302_FOUND)
    redirect_response.delete_cookie("access_token")
    return redirect_response


@router.get("/todo-page")
async def render_todo_page(request: Request, db: db_dependency):
    try:
        user = await get_current_user(request.cookies.get('access_token'))
        if user is None:
            return redirect_to_login()
        todos = db.query(Todo).filter(Todo.owner_id == user.get('id')).all()
        return templates.TemplateResponse("todo.html", {"request": request, "todos": todos, "user": user})
    except:
        return redirect_to_login()




@router.get("/")
async def read_all(user: user_dependency,db: db_dependency):
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="User is not found!")
    return db.query(Todo).filter(Todo.owner_id == user.get('id')).all()


@router.get("/todo/{todo_id}",status_code=status.HTTP_200_OK)
async def read_by_id(user: user_dependency,db: db_dependency,todo_id: int = Path(gt=0)):
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="User is not found!")
    todo = db.query(Todo).filter(Todo.id == todo_id).first()

    if todo is not None:
        return todo
    raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,detail = "Todo Not Found!")



@router.post("/todo",status_code=status.HTTP_201_CREATED)
async def create_todo(user: user_dependency,db: db_dependency,todo_request: TodoRequest):
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="User is not found!")
    todo = Todo(**todo_request.dict(),owner_id=user.get('id'))
    db.add(todo)
    db.commit() # dont forget


@router.put("/todo/{todo_id}")
async def update_todo(user: user_dependency,db:db_dependency, todo_request:TodoRequest, todo_id:int = Path(gt=0)):
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="User is not found!")
    todo = db.query(Todo).filter(Todo.id == todo_id).filter(Todo.owner_id == user.get('id')).first()
    if todo is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Todo is not found!")

    todo.title = todo_request.title
    todo.description = todo_request.description
    todo.priority = todo_request.priority
    todo.complete = todo_request.complete

    db.add(todo)
    db.commit()

@router.delete("/todo/{todo_id}",status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(user: user_dependency,db:db_dependency,todo_id:int = Path(gt=0)):
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="User is not found!")

    todo = db.query(Todo).filter(Todo.id == todo_id).filter(Todo.owner_id == user.get('id').first())
    if todo is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Todo is not found!")
    #for ensure to delete correct data
    db.delete(todo)
    db.commit()



