from enum import StrEnum
from pathlib import Path

from pydantic import PostgresDsn
from pydantic_settings import BaseSettings


class EnvironmentType(StrEnum):
    DEVELOPMENT = "development"
    PRODUCTION = "production"
    TEST = "test"


class BaseConfig(BaseSettings):
    class Config:
        case_sensitive = True
        env_file = Path(__file__).resolve().parent.parent / ".env"
        env_file_encoding = "utf-8"


class Config(BaseConfig):
    ENVIRONMENT: str = EnvironmentType.DEVELOPMENT
    POSTGRES_URL: PostgresDsn = PostgresDsn(
        "postgresql+asyncpg://user:password@127.0.0.1:5432/db-name"
    )



config = Config()

print(config.ENVIRONMENT)
print(config.POSTGRES_URL)
