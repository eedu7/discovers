from fastapi import APIRouter, Depends

from app.controllers import AuthController
from app.schemas.requests.users import RegisterUserRequest
from core.factory import Factory

router = APIRouter()


@router.post("/register")
async def register_user(
    user_data: RegisterUserRequest,
    auth_controller: AuthController = Depends(Factory().get_auth_controller),
):
    return await auth_controller.register(
        email=user_data.email, password=user_data.password, username=user_data.username
    )
