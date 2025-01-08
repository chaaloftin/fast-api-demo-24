from typing import Annotated, Literal, Optional
from pydantic import BaseModel, Field


class Item(BaseModel):
    id: int = Field(ge=1)
    name: str = Field(min_length=1)
    price: float = Field(ge=0)
    tax: Optional[Annotated[float, Field(ge=0.0)]] = 1.2
    description: Optional[Annotated[str, Field(max_length=50)]] = ""
