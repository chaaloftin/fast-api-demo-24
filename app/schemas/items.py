from typing import Union
from pydantic import BaseModel


class Item(BaseModel):
    id: int
    name: str
    price: float
    tax: Union[float, None] = None
    description: Union[str, None] = None
