from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

v1_router = APIRouter()


@v1_router.get("/")
async def home():
    return JSONResponse(
        {"title": "Discovers", "description": "API endpoints for the Discovers"},
        status_code=status.HTTP_200_OK,
    )
