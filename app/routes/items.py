from typing import Annotated, List, Union
from fastapi import APIRouter, Path, Query
from app.schemas import Item, ItemParams


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


@router.get("/")
async def get_all_items(
    min_price: float = 0.0, max_price: float = 1000000
) -> List[Item]:
    return [
        item for item in items if item.price > min_price and item.price <= max_price
    ]


@router.get("/{id}")
async def get_item(
    id: Annotated[int, Path(ge=1)],
    include_attributes: Annotated[Union[List[str], None], Query(max_length=3)] = None,
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
