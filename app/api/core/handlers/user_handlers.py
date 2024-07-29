from pydantic import EmailStr, BaseModel

from typing import Annotated

from fastapi import APIRouter, Path

from api.orm import User

router = APIRouter(prefix="/users", tags=["users"])


class UserCreate(BaseModel):
    email: EmailStr
    username: str


@router.get("/")
async def list_users():
    return [
        "User1",
        "User2",
        "User3",
    ]


@router.get("/{user_id}")
async def read_user(user_id: Annotated[int, Path(ge=0)]):
    return {"user_id": user_id}


@router.post("/register")
def create_user(user: UserCreate):
    return {
        "message": "User created!",
        "email": user.email,
        "username": user.username,
    }
