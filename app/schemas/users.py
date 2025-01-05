from typing import Literal, Union
from pydantic import BaseModel, Field

from app.core.constants import USER_DEFAULT_MAX_AGE, USER_DEFAULT_MIN_AGE


class User(BaseModel):
    name: str
    age: Union[int, None] = None


class UserParams(BaseModel):
    min_age: int = Field(USER_DEFAULT_MIN_AGE, ge=USER_DEFAULT_MIN_AGE)
    max_age: int = Field(USER_DEFAULT_MIN_AGE, ge=USER_DEFAULT_MAX_AGE)
    order_by: Literal["age", "name"] = "age"
