from typing import List

from fastapi import FastAPI
from starlette.middleware import Middleware

from api import router
from core.fastapi.middlewares.response_logger import ResponseLoggerMiddleware
from core.fastapi.middlewares.sqlalchemy import SQLAlchemyMiddleware


def init_router(app: FastAPI) -> None:
    app.include_router(router)


def make_middleware() -> List[Middleware]:
    return [Middleware(SQLAlchemyMiddleware), Middleware(ResponseLoggerMiddleware)]


def create_app() -> FastAPI:
    app = FastAPI(
        title="Discovers",
        description="API Route for Discovers",
        middleware=make_middleware(),
    )
    init_router(app)

    return app


app: FastAPI = create_app()
