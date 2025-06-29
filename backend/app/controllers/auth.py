
from pydantic import EmailStr

from app.exceptions import BadRequestException
from app.models import User
from app.repositories import UserRepository
from core.controller import BaseController
from core.database import Propagation, Transactional
from core.security import PasswordHandler


class AuthController(BaseController[User]):
    def __init__(self, user_repository: UserRepository):
        super().__init__(model=User, repository=user_repository)
        self.user_repository = user_repository

    @Transactional(propagation=Propagation.REQUIRED)
    async def register(self, *, email: EmailStr, password: str, username: str):
        user = await self.user_repository.user_exists(email=email)

        if user:
            raise BadRequestException("User already exists with this email.")

        user = await self.user_repository.user_exists(username=username)

        if user:
            raise BadRequestException("User already exists with this username.")

        hashed_password = PasswordHandler.hash(password)

        return await self.user_repository.create({"email": email, "password": hashed_password, "username": username})

    async def login(self, email: EmailStr, password: str):
        user: User = await self.user_repository.user_exists(email=email)

        if not user:
            raise BadRequestException("No account found with the provided email address.")

        if not PasswordHandler.verify(plain_password=password, hashed_password=user.password):
            raise BadRequestException("Incorrect password. Please try again.")

        # TODO: Generate and return JWT access and refresh token
