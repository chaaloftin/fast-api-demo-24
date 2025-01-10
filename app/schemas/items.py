from typing import Annotated, Optional
from pydantic import BaseModel, Field


class Item(BaseModel):
    id: int = Field(
        ge=1,
        title="Item ID",
        description="A unique identifier for the item. Must be 1 or greater.",
    )
    name: str = Field(
        min_length=1,
        title="Item Name",
        description="The name of the item. Must be at least 1 character long.",
    )
    price: float = Field(
        ge=0,
        title="Item Price",
        description="The price of the item. Must be 0 or greater.",
    )
    tax: Optional[Annotated[float, Field(ge=0.0)]] = Field(
        default=None,
        title="Item Tax",
        description="The tax applied to the item. Must be 0.0 or greater. This field is optional.",
    )
    description: Optional[Annotated[str, Field(max_length=50)]] = Field(
        default=None,
        title="Item Description",
        description="A short description of the item. Must not exceed 50 characters. This field is optional.",
    )
