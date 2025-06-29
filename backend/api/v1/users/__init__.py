from fastapi import APIRouter

from .users import router

user_router = APIRouter()

user_router.include_router(router)
