from typing import Literal

from pydantic import BaseModel, Field


class CheckUserExists(BaseModel):
    exists: bool = Field(..., description="Indicates whether a user with the given field and value exists.")
    field: Literal["email", "username"] = Field(
        ..., description="The field used to check user existence (username or email)."
    )
    value: str = Field(..., min_length=1, description="The value provided for the field being checked.")
