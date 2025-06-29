from functools import partial

from fastapi.params import Depends

from app.controllers import AuthController
from app.models import User
from app.repositories import UserRepository
from core.database import get_session


class Factory:
    user_repository = partial(UserRepository, User)

    def get_auth_controller(self, session=Depends(get_session)):
        return AuthController(user_repository=self.user_repository(session=session))
