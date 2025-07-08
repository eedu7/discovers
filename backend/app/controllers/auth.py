from pydantic import EmailStr

from app.models import User
from app.repositories import UserRepository
from app.schemas.extras import Token
from core.controller import BaseController
from core.database import Propagation, Transactional
from core.exceptions import BadRequestException
from core.security import JWTHandler, PasswordHandler


class AuthController(BaseController[User]):
    def __init__(self, user_repository: UserRepository):
        super().__init__(model=User, repository=user_repository)
        self.user_repository = user_repository

    @Transactional(propagation=Propagation.REQUIRED)
    async def register(self, *, email: EmailStr, password: str, username: str):
        if await self.user_repository.user_exists(email=email):
            raise BadRequestException("User already exists with this email.")

        if await self.user_repository.user_exists(username=username):
            raise BadRequestException("User already exists with this username.")

        hashed_password = PasswordHandler.hash(password)

        return await self.user_repository.create({"email": email, "password": hashed_password, "username": username})

    async def login(self, email: EmailStr, password: str):
        exists: bool = await self.user_repository.user_exists(email=email)

        if not exists:
            raise BadRequestException("No account found with the provided email address.")

        user: User = await self.user_repository.get_by_email(str(email))

        hashed_password: str = user.password

        if not PasswordHandler.verify(plain_password=password, hashed_password=hashed_password):
            raise BadRequestException("Incorrect password. Please try again.")

        payload = {
            "sub": str(user.id),
            "username": user.username,
            "email": user.email,
        }
        access_token = JWTHandler.encode(payload)
        refresh_token = JWTHandler.encode(payload, token_type="refresh")

        return Token(access_token=access_token, refresh_token=refresh_token)
