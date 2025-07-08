from http import HTTPStatus
from typing import List

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from starlette.middleware import Middleware

from api import router
from core.exceptions import CustomException
from core.fastapi.middlewares import (
    AuthBackend,
    AuthenticationMiddleware,
    ResponseLoggerMiddleware,
    SQLAlchemyMiddleware,
)


def on_auth_error(_: Request, exc: Exception | CustomException):
    if isinstance(exc, CustomException):
        status_code = exc.code
        error_code = exc.error_code
        message = exc.message
    else:
        status_code = HTTPStatus.UNAUTHORIZED
        error_code = None
        message = str(exc)

    return JSONResponse(status_code=status_code, content={"error_code": error_code, "message": message})


def init_router(app: FastAPI) -> None:
    app.include_router(router)


def init_listeners(app: FastAPI) -> None:
    @app.exception_handler(CustomException)
    async def custom_exception_handler(request: Request, exc: CustomException):
        return JSONResponse(status_code=exc.code, content={"error_code": exc.error_code, "message": exc.message})


def make_middleware() -> List[Middleware]:
    return [
        Middleware(
            CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"]
        ),
        Middleware(
            AuthenticationMiddleware,
            backend=AuthBackend(),
        ),
        Middleware(SQLAlchemyMiddleware),
        Middleware(ResponseLoggerMiddleware),
    ]


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
