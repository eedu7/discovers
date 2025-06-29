from typing import List

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from starlette.middleware import Middleware

from api import router
from app.exceptions import CustomException
from core.fastapi.middlewares.response_logger import ResponseLoggerMiddleware
from core.fastapi.middlewares.sqlalchemy import SQLAlchemyMiddleware


def init_router(app: FastAPI) -> None:
    app.include_router(router)


def init_listeners(app: FastAPI) -> None:
    @app.exception_handler(Exception)
    async def custom_exception_handler(request: Request, exc: CustomException):
        return JSONResponse(status_code=exc.code, content={"error_code": exc.error_code, "message": exc.message})


def make_middleware() -> List[Middleware]:
    return [Middleware(SQLAlchemyMiddleware), Middleware(ResponseLoggerMiddleware)]


def create_app() -> FastAPI:
    app = FastAPI(
        title="Discovers",
        description="API Route for Discovers",
        middleware=make_middleware(),
    )
    init_router(app)
    init_listeners(app)

    return app


app: FastAPI = create_app()
