from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
from .mixins import UserRelationMixin


class Profile(UserRelationMixin, Base):
    _user_id_unique = True
    _user_back_populates = "profile"

    first_name: Mapped[str | None] = mapped_column(String(50))
    last_name: Mapped[str | None] = mapped_column(String(50))
    bio: Mapped[str | None]

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id!r}, title={self.user_id!r})"

    def __repr__(self) -> str:
        return str(self)
