from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


if TYPE_CHECKING:
    from .review import Review
    from .profile import Profile
    from .user_book_association import UserBookAssociation


class User(Base):

    username: Mapped[str] = mapped_column(
        String(50), unique=True, index=True, nullable=False
    )
    email: Mapped[str] = mapped_column(
        String(50), unique=True, index=True, nullable=False
    )

    reviews: Mapped[list["Review"]] = relationship(back_populates="user")
    profile: Mapped["Profile"] = relationship(back_populates="user")

    books_details: Mapped[list["UserBookAssociation"]] = relationship(
        back_populates="user",
        cascade="all, delete-orphan",
    )

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id!r}, username={self.username!r})"

    def __repr__(self) -> str:
        return str(self)
