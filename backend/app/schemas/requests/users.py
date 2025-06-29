import re

from pydantic import BaseModel, EmailStr, field_validator


class LoginUserRequest(BaseModel):
    email: EmailStr
    password: str

    @field_validator("password")
    @classmethod
    def password_must_contain_special_characters(cls, v: str) -> str:
        if not re.search(r"[^a-zA-Z0-9]", v):
            raise ValueError("Password must contain special characters")
        if not re.search(r"[0-9]", v):
            raise ValueError("Password must contain numbers")
        if not re.search(r"[A-Z]", v):
            raise ValueError("Password must contain uppercase characters")
        if not re.search(r"[a-z]", v):
            raise ValueError("Password must contain lowercase characters")
        return v


class RegisterUserRequest(LoginUserRequest):
    username: str

    @field_validator("username")
    @classmethod
    def username_must_not_contain_special_characters(cls, v: str) -> str:
        if re.search(r"[^a-zA-Z0-9]", v):
            raise ValueError("Username must not contain special characters")
        return v
