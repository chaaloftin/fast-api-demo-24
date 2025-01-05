from typing import Annotated, Any, Dict, Union
from xml.etree.ElementInclude import include
from fastapi import APIRouter, Path, Query
from app.schemas import User

router = APIRouter()

@router.get("/me")
async def get_user_me() -> User:
    return User(
        name="My user"
    )

@router.get("/{id}")
async def get_user(
    id: Annotated[int, Path(title="The id of the user", ge=1)],
    min_age: Annotated[Union[int,  None], Query(ge=1)] = None,
    max_age: Annotated[Union[int, None], Query(ge=1)] = None
    ) -> User:
    return User(name="Jane Doe", age=20)

@router.put("/{id}")
async def update_user(
    id: Annotated[int, Path(title="The id of  the user", ge=1)],
    user: User,
    include_deleted: Annotated[bool, Query()] = False
) -> Dict[str, Any]:
    result = {"id": id, **user.model_dump()}

    if include_deleted:
        result.update({"is_deleted": True})

    return result