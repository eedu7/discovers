from fastapi import FastAPI
from api import router


def init_router(app: FastAPI) -> None:
    app.include_router(router)


def create_app() -> FastAPI:
    app = FastAPI(title="Discovers", description="API Route for Discovers")
    init_router(app)
    return app


app: FastAPI = create_app()
