from typing import Any, Generic, Type, TypeVar

from core.database.session import Base
from core.database.transactional import Propagation, Transactional
from core.repository.base import BaseRepository

ModelType = TypeVar("ModelType", bound=Base)


class BaseController(Generic[ModelType]):
    def __init__(self, model: Type[ModelType], repository: BaseRepository) -> None:
        self.model = model
        self.repository = repository

    async def get_all(self, skip: int = 0, limit: int = 100):
        response = await self.repository.get_all(skip, limit)
        return response

    @Transactional(propagation=Propagation.REQUIRED)
    async def create(self, attributes: dict[str, Any]):
        create = await self.repository.create(attributes)

        return create
