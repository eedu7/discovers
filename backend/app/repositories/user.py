from typing import Dict

from pydantic import EmailStr
from sqlalchemy import exists, select

from app.models import User
from core.repository import BaseRepository


class UserRepository(BaseRepository[User]):
    async def user_exists(self, *, email: EmailStr | None = None, username: str | None = None) -> Dict[str, bool]:
        result = {}

        if email:
            query = select(exists().where(User.email == email))
            result["email_exists"] = await self.session.scalar(query)
        if username:
            query = select(exists().where(User.username == username))
            result["username_exists"] = await self.session.scalar(query)

        return result
