from app.models import User
from app.repositories import UserRepository
from core.controller import BaseController
from core.database import Propagation, Transactional


class AuthController(BaseController[User]):
    def __init__(self, user_repository: UserRepository):
        super().__init__(model=User, repository=user_repository)
        self.user_repository = user_repository

    @Transactional(propagation=Propagation.REQUIRED)
    async def register(self, email: str, password: str, username: str):
        return await self.user_repository.create(
            {"email": email, "password": password, "username": username}
        )
