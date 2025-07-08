from pydantic import EmailStr

from app.models import User
from app.repositories import UserRepository
from app.schemas.response.user import CheckUserExists
from core.controller import BaseController


class UserController(BaseController[User]):
    def __init__(self, user_repository: UserRepository):
        super().__init__(model=User, repository=user_repository)
        self.user_repository = user_repository

    async def check_user_exists(self, email: EmailStr | None = None, username: str | None = None) -> CheckUserExists:
        if not email and not username:
            raise ValueError(
                "Missing required input: at least one of 'email' or 'username' must be"
                " provided to check if the user exists."
            )

        if email:
            exists = await self.user_repository.user_exists(email=email)
            return CheckUserExists(exists=exists, field="email", value=str(email))
        else:
            exists = await self.user_repository.user_exists(username=username)
            return CheckUserExists(exists=exists, field="username", value=username)
