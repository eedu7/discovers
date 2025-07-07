from pydantic import EmailStr
from sqlalchemy import exists, select

from app.models import User
from core.repository import BaseRepository


class UserRepository(BaseRepository[User]):
    async def user_exists(self, *, email: EmailStr | None = None, username: str | None = None) -> bool:
        if email:
            query = select(exists().where(User.email == email))
            return await self.session.scalar(query)
        else:
            query = select(exists().where(User.username == username))
            return await self.session.scalar(query)

    async def get_by_email(self, email: str) -> User | None:
        return await self.get_by(field="email", value=email, unique=True)

    async def get_by_username(self, username: str) -> User | None:
        return await self.get_by(field="username", value=username, unique=True)
