from typing import Tuple

from jose import JWTError
from starlette.authentication import AuthenticationBackend
from starlette.middleware.authentication import AuthenticationMiddleware as BaseAuthenticationMiddleware
from starlette.requests import HTTPConnection

from app.schemas.extras import CurrentUser
from core.security import JWTHandler


class AuthBackend(AuthenticationBackend):
    async def authenticate(self, conn: HTTPConnection) -> Tuple[bool, CurrentUser]:
        current_user = CurrentUser()
        authorization: str = conn.headers.get("Authorization")
        if not authorization:
            return False, current_user

        try:
            scheme, token = authorization.split(" ")
            if scheme.lower() != "bearer":
                return False, current_user

        except ValueError:
            return False, current_user

        if not token:
            return False, current_user

        try:
            payload = JWTHandler.decode(token)
            # TODO: Change to UUID, after changing the CurrentUser ID to "UUID", also updating the "Token" payload
            user_id = payload.get("user_id")
        except JWTError:
            return False, current_user

        # TODO: Change to UUID
        current_user.id = user_id
        return True, current_user


class AuthenticationMiddleware(BaseAuthenticationMiddleware):
    pass
