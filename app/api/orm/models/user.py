from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from .review import Review


class User(Base):

    first_name: Mapped[str] = mapped_column(String(50))
    last_name: Mapped[str] = mapped_column(String(50))
    username: Mapped[str] = mapped_column(
        String(50), unique=True, index=True, nullable=False
    )
    email: Mapped[str] = mapped_column(
        String(50), unique=True, index=True, nullable=False
    )

    reviews: Mapped[list["Review"]] = relationship(back_populates="user")

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, fullname={self.first_name!r}{self.last_name!r})"
