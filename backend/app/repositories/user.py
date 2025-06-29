from pydantic import EmailStr
from sqlalchemy import exists, or_, select

from app.models import User
from core.repository import BaseRepository


class UserRepository(BaseRepository[User]):
    async def user_exists(self, *, email: EmailStr | None, username: str | None = None):
        if not email or not username:
            raise ValueError(
                "Missing required input: at least one of 'email' or 'username' must be"
                " provided to check if the user exists."
            )

        conditions = []

        if email:
            conditions.append(User.email == email)
        if username:
            conditions.append(User.username == username)

        query = select(exists().where(or_(*conditions)))
        return await self.session.scalar(query)
