from uuid import uuid4

from sqlalchemy import BigInteger, Unicode
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from core.database.session import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    uuid: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True), default=uuid4(), unique=True, nullable=False
    )
    email: Mapped[str] = mapped_column(
        Unicode(255), nullable=False, unique=True, index=True
    )
    username: Mapped[str] = mapped_column(Unicode(255), nullable=False, unique=True)
    password: Mapped[str] = mapped_column(Unicode(255), nullable=False)

    def __str__(self):
        return f"UUID: {self.uuid}, email: {self.email}, username: {self.username}"

    def __repr__(self):
        return self.__str__()
