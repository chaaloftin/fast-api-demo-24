from pydantic import BaseModel, Field


class Order(BaseModel):
    id: int = Field(
        ge=1,
        title="Order ID",
        description="A unique identifier for the order. Must be 1 or greater.",
    )
    user_id: int = Field(
        ge=1,
        title="User ID",
        description="The unique identifier of the user who placed the order. Must be 1 or greater.",
    )
    item_id: int = Field(
        ge=1,
        title="Item ID",
        description="The unique identifier of the item in the order. Must be 1 or greater.",
    )
    quantity: float = Field(
        ge=1,
        title="Order Quantity",
        description="The quantity of the item in the order. Must be 1 or greater.",
    )
