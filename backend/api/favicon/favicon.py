import os

from fastapi import APIRouter
from starlette.responses import FileResponse

favicon_router = APIRouter()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(BASE_DIR, "assets")


@favicon_router.get("/favicon.ico", include_in_schema=False)
async def favicon():
    favicon_path = os.path.join(ASSETS_DIR, "favicon.ico")
    return FileResponse(favicon_path)
