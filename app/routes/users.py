from typing import Union
from fastapi import APIRouter
from app.schemas import User

router = APIRouter()

@router.get("/me")
async def get_user_me() -> User:
    return User(
        name="My user"
    )

@router.get("/{user_id}")
async def get_user(user_id, min_age: Union[int,  None] = None, max_age: Union[int, None] = None) -> User:
    return User(name="Jane Doe", age=20)