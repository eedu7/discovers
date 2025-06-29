from typing import Any, Dict, Generic, Type, TypeVar

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.expression import select

from core.database.session import Base

ModelType = TypeVar("ModelType", bound=Base)


class BaseRepository(Generic[ModelType]):
    def __init__(self, model: Type[ModelType], session: AsyncSession) -> None:
        self.session = session
        self.model = model

    async def create(self, attributes: Dict[str, Any] | None = None) -> ModelType:
        if attributes is None:
            attributes = {}

        model = self.model(**attributes)
        self.session.add(model)
        return model

    async def get_all(self, skip: int = 0, limit: int = 10):
        query = select(self.model).offset(skip).limit(limit)
        query = await self.session.scalars(query)
        return query.all()
