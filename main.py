from fastapi import FastAPI
from models import Base,User, Todo
from database import engine
from routers.todo import router as todo_router
from routers.auth import router as auth_router

app = FastAPI()

app.include_router(auth_router)
app.include_router(todo_router)

Base.metadata.create_all(bind=engine)
