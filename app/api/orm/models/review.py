from typing import TYPE_CHECKING
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
from .mixins import UserRelationMixin


class Review(UserRelationMixin, Base):
    _user_back_populates = "reviews"

    title: Mapped[str] = mapped_column(String(50), unique=False)
    body: Mapped[str] = mapped_column(String(100))

    def __repr__(self) -> str:
        return f"Review(id={self.id!r}, title={self.title!r}, user_id={self.user_id!r})"
