from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from pydantic import EmailStr

from app.controllers import AuthController, UserController
from core.factory import Factory
from core.fastapi.dependencies import AuthenticationRequired

router = APIRouter()


@router.get("/", dependencies=[Depends(AuthenticationRequired)])
async def get_all(
    auth_controller: AuthController = Depends(Factory().get_auth_controller),
):
    return await auth_controller.get_all()


@router.get("/exists")
async def check_user_exists(
    username: str | None = None,
    email: EmailStr | None = None,
    user_controller: UserController = Depends(Factory().get_user_controller),
) -> JSONResponse:
    return await user_controller.check_user_exists(email, username)
