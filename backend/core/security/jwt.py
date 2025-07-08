from http import HTTPStatus
from typing import Any, Dict, Literal

from jose import ExpiredSignatureError, JWTError, jwt

from core.config import config
from core.exceptions import CustomException
from core.utils import get_timestamp


class JWTDecodeError(CustomException):
    code = HTTPStatus.UNAUTHORIZED
    message = "Invalid token"


class JWTExpiredError(CustomException):
    code = HTTPStatus.UNAUTHORIZED
    message = "Token expired"


TokenType = Literal["access", "refresh"]


class JWTHandler:
    secret_key: str = config.JWT_SECRET_KEY
    algorithm: str = config.JWT_ALGORITHM
    access_token_expiry: int = config.JWT_ACCESS_TOKEN_EXPIRE_MINUTES
    refresh_token_expiry: int = config.JWT_REFRESH_TOKEN_EXPIRE_MINUTES

    @classmethod
    def encode(cls, payload: Dict[str, Any], token_type: TokenType = "access") -> str:
        expire_minutes: int = cls.access_token_expiry if token_type == "access" else cls.refresh_token_expiry

        expire = get_timestamp(minutes=expire_minutes)
        iat = get_timestamp()
        payload.update({"exp": expire, "iat": iat, "token_type": token_type})
        return jwt.encode(payload, cls.secret_key, algorithm=cls.algorithm)

    @classmethod
    def decode(cls, token: str, verify_exp: bool = True) -> Dict[str, Any]:
        try:
            return jwt.decode(token, cls.secret_key, algorithms=[cls.algorithm], options={"verify_exp": verify_exp})
        except ExpiredSignatureError as e:
            raise JWTExpiredError() from e
        except JWTError as e:
            raise JWTDecodeError() from e
