from fastapi import APIRouter, Depends, status

from app.controllers import AuthController
from app.schemas.requests.auth import LoginUserRequest, RegisterUserRequest
from app.schemas.response.auth import LoginUserResponse, RegisterUserResponse
from core.factory import Factory

router = APIRouter()


@router.post("/register", status_code=status.HTTP_201_CREATED, response_model=RegisterUserResponse)
async def register(
    user_data: RegisterUserRequest,
    auth_controller: AuthController = Depends(Factory().get_auth_controller),
):
    return await auth_controller.register(
        email=user_data.email, password=user_data.password, username=user_data.username
    )


@router.post("/login", response_model=LoginUserResponse, status_code=status.HTTP_200_OK)
async def login(user_data: LoginUserRequest, auth_controller: AuthController = Depends(Factory().get_auth_controller)):
    return await auth_controller.login(email=user_data.email, password=user_data.password)
