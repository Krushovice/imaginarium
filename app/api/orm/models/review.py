from typing import TYPE_CHECKING
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from .user import User


class Review(Base):

    title: Mapped[str] = mapped_column(String(50), unique=False)
    body: Mapped[str] = mapped_column(String(100))

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    user: Mapped["User"] = relationship(back_populates="reviews")

    def __repr__(self) -> str:
        return f"Review(id={self.id!r}, title={self.title!r}, user_id={self.user_id!r})"
