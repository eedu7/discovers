from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from pydantic import EmailStr

from app.controllers import AuthController, UserController
from app.schemas.response.user import CheckUserExists
from core.exceptions import UnprocessableEntity
from core.factory import Factory
from core.fastapi.dependencies import AuthenticationRequired

router = APIRouter()


@router.get("/", dependencies=[Depends(AuthenticationRequired)])
async def get_all(
    auth_controller: AuthController = Depends(Factory().get_auth_controller),
):
    return await auth_controller.get_all()


@router.get("/exists", status_code=status.HTTP_200_OK, response_model=CheckUserExists)
async def check_user_exists(
    username: str | None = None,
    email: EmailStr | None = None,
    user_controller: UserController = Depends(Factory().get_user_controller),
):
    if not username and not email:
        raise UnprocessableEntity("Either 'username' or 'email' must be provided to check existence.")
    return await user_controller.check_user_exists(email, username)
