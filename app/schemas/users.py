from typing import Literal, Optional
from pydantic import BaseModel, Field


class User(BaseModel):
    name: str = Field(title="User Name", description="The name of the user.")
    age: Optional[int] = Field(
        default=None,
        title="User Age",
        description="The age of the user. This field is optional.",
    )


class UserParams(BaseModel):
    min_age: int = Field(
        default=0,
        ge=0,
        title="Minimum Age",
        description="The minimum age of the users to include in the results. Must be 0 or greater.",
    )
    max_age: int = Field(
        default=100,
        ge=0,
        title="Maximum Age",
        description="The maximum age of the users to include in the results. Must be 0 or greater.",
    )
    order_by: Literal["age", "name"] = Field(
        default="age",
        title="Order By",
        description='The field to order the results by. Options are "age" or "name".',
    )
