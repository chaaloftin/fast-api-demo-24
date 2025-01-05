from typing import Any, Dict, Union
from xml.etree.ElementInclude import include
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

@router.put("/{user_id}")
async def update_user(user_id: int, user: User, include_deleted: bool = False) -> Dict[str, Any]:
    result = {"user_id": user_id, **user.model_dump()}

    if include_deleted:
        result.update({"is_deleted": True})

    return result