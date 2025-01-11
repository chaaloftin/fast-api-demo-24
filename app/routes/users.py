from typing import Annotated, Any, Dict, List, Optional, Union
from xml.etree.ElementInclude import include
from fastapi import APIRouter, Body, Path, Query
from app.schemas import User, Item

router = APIRouter()


@router.get("/me")
async def get_user_me() -> User:
    return User(name="My user")


@router.get("/{id}")
async def get_user(
    id: Annotated[int, Path(description="The target object's ID", ge=1)],
    min_age: Optional[Annotated[int, Query(ge=1)]] = None,
    max_age: Optional[Annotated[int, Query(ge=1)]] = None,
) -> User:
    return User(name="Jane Doe", age=20)


@router.get("/{id}/orders")
async def get_user_items(
    id: Annotated[int, Path(description="The target object's ID", ge=1)]
) -> List[Item]:
    return [Item(id=id, name="item", price=1.0)]


@router.put("/{id}")
async def update_user(
    id: Annotated[int, Path(description="The target object's ID", ge=1)],
    user: Annotated[User, Body()],
) -> Dict[str, Any]:
    result = {"id": id, **user.model_dump()}

    return result
