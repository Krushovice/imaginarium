from typing import TYPE_CHECKING
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
from .mixins import UserRelationMixin

if TYPE_CHECKING:
    from app.api.orm import UserBookAssociation


class Profile(UserRelationMixin, Base):
    _user_id_unique = True
    _user_back_populates = "profile"

    first_name: Mapped[str | None] = mapped_column(String(50))
    last_name: Mapped[str | None] = mapped_column(String(50))
    favorite_genre: Mapped[str] = mapped_column(String(25), nullable=True)

    books_details: Mapped[list["UserBookAssociation"]] = relationship(
        back_populates="profile",
        cascade="all, delete-orphan",
    )

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id!r}, title={self.user_id!r})"

    def __repr__(self) -> str:
        return str(self)
