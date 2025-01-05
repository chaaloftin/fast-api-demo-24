from typing import Literal, Union
from pydantic import BaseModel, Field

from app.core.constants import ITEM_DEFAULT_MAX_PRICE, ITEM_DEFAULT_MIN_PRICE


class Item(BaseModel):
    id: int
    name: str
    price: float
    tax: Union[float, None] = None
    description: Union[str, None] = None


class ItemParams(BaseModel):
    # Forbid extra attributes
    model_config = {"extra": "forbid"}

    min_price: int = Field(ITEM_DEFAULT_MIN_PRICE, ge=ITEM_DEFAULT_MIN_PRICE)
    max_price: int = Field(ITEM_DEFAULT_MAX_PRICE, ge=ITEM_DEFAULT_MAX_PRICE)
    order_by: Literal["price", "name"] = "price"
