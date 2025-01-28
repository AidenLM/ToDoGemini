from alembic.util import status
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from starlette.responses import RedirectResponse
from starlette import status
from models import Base,User, Todo
from database import engine
from routers.todo import router as todo_router
from routers.auth import router as auth_router

app = FastAPI()

app.mount("/static",StaticFiles(directory="static"),name= "static")


@app.get("/") #static file is introduced to main app
def read_root(request: Request):
    return RedirectResponse(url="/todo/todo-page", status_code= status.HTTP_302_FOUND)



app.include_router(auth_router)
app.include_router(todo_router)

Base.metadata.create_all(bind=engine)
