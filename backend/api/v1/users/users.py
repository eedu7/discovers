from fastapi import APIRouter, Depends

from app.controllers import AuthController
from core.factory import Factory
from core.fastapi.dependencies import AuthenticationRequired

router = APIRouter()


@router.get("/", dependencies=[Depends(AuthenticationRequired)])
async def get_all(
    auth_controller: AuthController = Depends(Factory().get_auth_controller),
):
    return await auth_controller.get_all()
