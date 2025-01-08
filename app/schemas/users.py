from typing import Annotated, Literal, Optional, Union
from pydantic import BaseModel, Field


class User(BaseModel):
    name: str
    age: Optional[int] = None


class UserParams(BaseModel):
    min_age: Optional[Annotated[int, Field(ge=0)]] = 0
    max_age: Optional[Annotated[int, Field(ge=100)]] = 0
    order_by: Literal["age", "name"] = "age"
