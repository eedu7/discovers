from uuid import UUID

from pydantic import BaseModel, EmailStr, Field

from app.schemas.extras import Token


class RegisterUserResponse(BaseModel):
    uuid: UUID = Field(..., description="UUID of the user", examples=["bb07ccbc-9039-425b-9863-01f7ca03c4fd"])
    email: EmailStr = Field(..., description="Email address of the user", examples=["john.doe@example.com"])
    username: str = Field(..., description="Username of the user", examples=["john.doe"])


class LoginUserResponse(Token):
    pass
