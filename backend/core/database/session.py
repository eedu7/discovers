from contextvars import ContextVar, Token
from typing import Any

from sqlalchemy import ClauseElement, Connection, Engine
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_scoped_session,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm.session import _EntityBindKey, _SessionBind
from sqlalchemy.sql.expression import Delete, Insert, Update

from core.config import config

session_context: ContextVar[str] = ContextVar("session_context")


def get_session_context() -> str:
    return session_context.get()


def set_session_context(session_id: str) -> Token:
    return session_context.set(session_id)


def reset_session_context(context: Token) -> None:
    session_context.reset(context)


engines = {
    "writer": create_async_engine(str(config.POSTGRES_URL), pool_recycle=3600),
    "reader": create_async_engine(str(config.POSTGRES_URL), pool_recycle=3600),
}


class RoutingAsyncSession(AsyncSession):
    def get_bind(
        self,
        mapper: _EntityBindKey | None = None,
        clause: ClauseElement | None = None,
        bind: _SessionBind | None = None,
        **kwargs: Any,
    ) -> Engine | Connection:
        if isinstance(clause, (Insert, Update, Delete)):
            return engines["writer"].sync_engine
        return engines["reader"].sync_engine


async_session_factory = async_sessionmaker(
    class_=RoutingAsyncSession,
    expire_on_commit=False,
)

session: AsyncSession | async_scoped_session = async_scoped_session(
    session_factory=async_session_factory,
    scopefunc=get_session_context,
)


async def get_session():
    try:
        yield session
    finally:
        await session.close()


Base = declarative_base()
