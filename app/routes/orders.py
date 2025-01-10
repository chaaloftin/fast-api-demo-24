from http import HTTPStatus
from typing import Annotated, List, Optional
from fastapi import APIRouter, HTTPException, Path, Query

from app.schemas import Order

router = APIRouter()

ORDERS = [
    Order(id=1, user_id=1, item_id=1, quantity=1.0),
    Order(id=2, user_id=1, item_id=2, quantity=2.0),
    Order(id=3, user_id=2, item_id=3, quantity=3.0),
]


@router.get("/{id}")
async def get_orders(
    id: Annotated[int, Path(description="The target object's ID", ge=1)],
    user_id: Optional[
        Annotated[int, Query(description="The ID of the user", default=None, ge=1)]
    ],
    item_id: Optional[
        Annotated[int, Query(description="The ID of the item", ge=1)]
    ] = None,
) -> List[Order]:
    orders = [order for order in ORDERS if order.id == id]

    if not orders:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND.value, detail="Order not found"
        )

    if user_id:
        orders = [order for order in orders if order.user_id == user_id]
    if item_id:
        orders = [order for order in orders if order.item_id == item_id]

    return orders
