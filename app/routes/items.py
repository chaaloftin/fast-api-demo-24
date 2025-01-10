from typing import Annotated, List, Optional, Union
from fastapi import APIRouter, Body, Path, Query
from pydantic import Field
from app.schemas import Item


router = APIRouter()
items = [Item(id=1, name="Spam", price=1.0), Item(id=2, name="Juice", price=2.0)]

# Leaving this here as an example of various types of query params
# @router.get("/")
# async def get_all_items(
#     required_q: Annotated[
#         Union[str, None], Query(alias="required-q", max_length=10, deprecated=True)
#     ] = None,
#     q: Annotated[
#         Union[str, None], Query(min_length=1, max_length=50, deprecated=True)
#     ] = None,
#     q_list: Annotated[
#         Union[List[str], None], Query(alias="q-list", deprecated=True)
#     ] = [],
#     hidden_q: Annotated[Union[str, None], Query(include_in_schema=False)] = None,
# ) -> Dict[str, Union[List[Item], str, List[str]]]:
#     results: dict = {
#         "items": [Item(id=1, name="Spam", price=1.0)],
#         "required_q": required_q,
#     }

#     if q:
#         results.update({"q": q})
#     if q_list:
#         results.update({"q_list": q_list})

#     return results


items = [
    Item(id=1, name="apple", price=0.5, tax=0.5, description="a single apple"),
    Item(id=2, name="juice", price=1.0, tax=0.5, description="a carton of juice"),
]


@router.get("/")
async def get_items(
    min_price: Annotated[
        float, Query(description="The minimum price for the items")
    ] = 0.0,
    max_price: Annotated[
        float, Query(description="The maximum pricee for the items")
    ] = 0.0,
) -> List[Item]:
    return [
        item for item in items if item.price > min_price and item.price <= max_price
    ]


@router.get("/{id}")
async def get_item(
    id: Annotated[int, Path(description="The target object's ID", ge=1)],
    include_attributes: Optional[
        Annotated[
            List[str],
            Query(
                description="The list of attributes to include.  All others are excluded.",
                min_length=1,
            ),
        ]
    ] = None,
):
    result: dict = {
        "item": Item(id=id, name="soup", price=5.0).model_dump(),
    }

    if include_attributes:
        result.update({attribute: attribute for attribute in include_attributes})

    return result


@router.post("/")
async def create_item(
    item: Annotated[Item, Body(description="The data for the user")]
) -> Item:
    return item
