from functools import reduce
from typing import Any, Generic, Type, TypeVar

from sqlalchemy import Select, func
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.expression import select

from core.database import Base

ModelType = TypeVar("ModelType", bound=Base)


class BaseRepository(Generic[ModelType]):
    def __init__(self, model: Type[ModelType], session: AsyncSession):
        self.session = session
        self.model_class: Type[ModelType] = model

    async def create(self, attributes: dict[str, Any] = None) -> ModelType:
        if attributes is None:
            attributes = {}
        model = self.model_class(**attributes)
        self.session.add(model)
        return model

    async def get_all(self, skip: int = 0, limit: int = 100, join_: set[str] | None = None) -> list[ModelType]:
        query = self._query(join_)
        query = query.offset(skip).limit(limit)

        if join_ is not None:
            return await self.all_unique(query)

        return await self._all(query)

    async def get_by(
        self,
        field: str,
        value: Any,
        join_: set[str] | None = None,
        unique: bool = False,
    ) -> ModelType:
        query = self._query(join_)
        query = await self._get_by(query, field, value)

        if join_ is not None:
            return await self.all_unique(query)
        if unique:
            return await self._one(query)

        return await self._all(query)

    async def delete(self, model: ModelType) -> None:
        self.session.delete(model)

    def _query(
        self,
        join_: set[str] | None = None,
        order_: dict | None = None,
    ) -> Select:
        query = select(self.model_class)
        query = self._maybe_join(query, join_)
        query = self._maybe_ordered(query, order_)

        return query

    async def _all(self, query: Select) -> list[ModelType]:
        query = await self.session.scalars(query)
        return query.all()

    async def _all_unique(self, query: Select) -> list[ModelType]:
        result = await self.session.execute(query)
        return result.unique().scalars().all()

    async def _first(self, query: Select) -> ModelType | None:
        query = await self.session.scalars(query)
        return query.first()

    async def _one_or_none(self, query: Select) -> ModelType | None:
        query = await self.session.scalars(query)
        return query.one_or_none()

    async def _one(self, query: Select) -> ModelType:
        query = await self.session.scalars(query)
        return query.one()

    async def _count(self, query: Select) -> int:
        query = query.subquery()
        query = await self.session.scalars(select(func.count()).select_from(query))
        return query.one()

    async def _sort_by(
        self,
        query: Select,
        sort_by: str,
        order: str | None = "asc",
        model: Type[ModelType] | None = None,
        case_insensitive: bool = False,
    ) -> Select:
        model = model or self.model_class

        order_column = None

        if case_insensitive:
            order_column = func.lower(getattr(model, sort_by))
        else:
            order_column = getattr(model, sort_by)

        if order == "desc":
            return query.order_by(order_column.desc())

        return query.order_by(order_column.asc())

    async def _get_by(self, query: Select, field: str, value: Any) -> Select:
        return query.where(getattr(self.model_class, field) == value)

    def _maybe_join(self, query: Select, join_: set[str] | None = None) -> Select:
        if not join_:
            return query

        if not isinstance(join_, set):
            raise TypeError("join_ must be a set")

        return reduce(self._add_join_to_query, join_, query)

    def _maybe_ordered(self, query: Select, order_: dict | None = None) -> Select:
        if order_:
            if order_["asc"]:
                for order in order_["asc"]:
                    query = query.order_by(getattr(self.model_class, order).asc())
            else:
                for order in order_["desc"]:
                    query = query.order_by(getattr(self.model_class, order).desc())

        return query

    def _add_join_to_query(self, query: Select, join_: set[str]) -> Select:
        return getattr(self, "_join_" + join_)(query)
