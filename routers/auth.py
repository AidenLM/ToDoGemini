from fastapi import APIRouter
from pydantic import BaseModel

from models import User

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)

# create request
class CreateUserRequest(BaseModel):
    username: str
    email: str
    first_name: str
    last_name: str
    password: str
    role: str


@router.post("/auth")
async def create_user(create_user_request: CreateUserRequest):
    user = User()
