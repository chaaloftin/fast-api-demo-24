import re
from typing import Annotated, Any, Dict, List, Union
from xml.etree.ElementInclude import include
from fastapi import APIRouter, Path, Query

router = APIRouter()

from app.schemas import Item

@router.get("/")
async def get_all_items(
    required_q: Annotated[str, Query(alias="required-q", max_length=10)],
    q: Annotated[Union[str, None], Query(min_length=1, max_length=50)] = None,
    q_list: Annotated[Union[List[str], None], Query(alias="q-list", deprecated=True)] = None,
    hidden_q: Annotated[Union[str, None], Query(deprecated=True, include_in_schema=False)] = None
) -> Dict[str, Union[List[Item], str, List[str]]]:
    results: dict = {"items": [Item(id=1, name="Spam", price=1.0)], "required_q": required_q}

    if q:
        results.update({"q": q})
    if q_list:
        results.update({"q_list": q_list})

    return results

@router.get("/{id}")
async def get_item(
    id: Annotated[int, Path(ge=1)],
    include_attributes: Annotated[Union[List[str], None], Query(max_length=3)] = None
):
    result: dict = {
        "item": Item(id=id, name="soup", price=5.0).model_dump(),
    }

    if include_attributes:
        result.update({attribute: attribute for attribute in include_attributes})

    return result

@router.post("/")
async def create_item(item: Item) -> Item:
    return item

