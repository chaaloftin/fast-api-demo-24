from typing import Annotated, Optional
from pydantic import BaseModel, Field


class Order(BaseModel):
    id: int = Field(ge=1)
    user_id: int = Field(ge=1)
    item_id: int = Field(ge=1)
    quantity: float = Field(ge=1)


class OrderParams(BaseModel):
    user_id: Optional[Annotated[int, Field(ge=1)]] = 0
    item_id: Optional[Annotated[int, Field(ge=1)]]
