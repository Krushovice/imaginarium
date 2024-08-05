from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from .user_book_association import UserBookAssociation


class Book(Base):

    title: Mapped[str] = mapped_column(String(50))
    author: Mapped[str] = mapped_column(String(50))
    genre: Mapped[str] = mapped_column(String(20))
    users_details: Mapped[list["UserBookAssociation"]] = relationship(
        back_populates="book",
        cascade="all, delete-orphan",
    )

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id!r}, title={self.title!r})"

    def __repr__(self) -> str:
        return str(self)
