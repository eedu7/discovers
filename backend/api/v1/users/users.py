from fastapi import APIRouter, Depends

from app.controllers import AuthController
from core.factory import Factory

router = APIRouter()


@router.get("/register")
async def register_user(
    auth_controller: AuthController = Depends(Factory().get_auth_controller),
):
    return await auth_controller.register(
        email="john.doe@gmail.com", password="password", username="John Doe"
    )


@router.get("/")
async def get_all(
    auth_controller: AuthController = Depends(Factory().get_auth_controller),
):
    return await auth_controller.get_all()
