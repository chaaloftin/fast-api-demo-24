from http import HTTPStatus
from typing import Annotated
from fastapi import APIRouter, HTTPException, Path, Query

from app.schemas import Order, OrderParams

router = APIRouter()

ORDERS = [
    Order(id=1, user_id=1, item_id=1, quantity=1.0),
    Order(id=2, user_id=1, item_id=2, quantity=2.0),
    Order(id=3, user_id=2, item_id=3, quantity=3.0),
]


@router.get("/{id}")
async def get_orders(
    id: Annotated[int, Path(ge=1)], params: Annotated[OrderParams, Query()]
) -> Order:
    order = next(order for order in ORDERS if order.id == id)

    if not order:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND.value, detail="Order not found"
        )
    return order
