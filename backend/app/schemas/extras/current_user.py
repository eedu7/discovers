from pydantic import BaseModel, Field


# TODO: Change to UUID
class CurrentUser(BaseModel):
    id: int = Field(None, description="User ID")

    class Config:
        validate_assignment = True
