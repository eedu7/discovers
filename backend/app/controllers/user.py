from fastapi import status
from fastapi.responses import JSONResponse
from pydantic import EmailStr

from app.models import User
from app.repositories import UserRepository
from core.controller import BaseController


class UserController(BaseController[User]):
    def __init__(self, user_repository: UserRepository):
        super().__init__(model=User, repository=user_repository)
        self.user_repository = user_repository

    async def check_user_exists(self, email: EmailStr | None = None, username: str | None = None) -> JSONResponse:
        if not email and not username:
            raise ValueError(
                "Missing required input: at least one of 'email' or 'username' must be"
                " provided to check if the user exists."
            )

        exists = await self.user_repository.user_exists(email=email, username=username)

        if not exists:
            return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "User does not exists"})

        return JSONResponse(status_code=status.HTTP_200_OK, content=exists)
