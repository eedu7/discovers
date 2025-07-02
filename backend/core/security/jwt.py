from datetime import UTC, datetime, timedelta
from http import HTTPStatus
from typing import Any, Dict

from jose import ExpiredSignatureError, JWTError, jwt

from core.config import config
from core.exceptions import CustomException


class JWTDecodeError(CustomException):
    code = HTTPStatus.UNAUTHORIZED
    message = "Invalid token"


class JWTExpiredError(CustomException):
    code = HTTPStatus.UNAUTHORIZED
    message = "Token expired"


class JWTHandler:
    secret_key = config.JWT_SECRET_KEY
    algorithm = config.JWT_ALGORITHM
    expire_minutes = config.JWT_EXPIRE_MINUTES

    @classmethod
    def encode(cls, payload: Dict[str, Any]) -> str:
        expire = datetime.now(UTC) + timedelta(minutes=cls.expire_minutes)
        payload.update({"exp": expire})
        return jwt.encode(payload, cls.secret_key, algorithm=cls.algorithm)

    @classmethod
    def decode(cls, token: str, verify_exp: bool = True) -> Dict[str, Any]:
        try:
            return jwt.decode(token, cls.secret_key, algorithms=[cls.algorithm], options={"verify_exp": verify_exp})
        except ExpiredSignatureError as e:
            raise JWTExpiredError() from e
        except JWTError as e:
            raise JWTDecodeError() from e
