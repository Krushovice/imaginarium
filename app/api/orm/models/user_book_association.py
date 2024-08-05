from enum import Enum
from typing import TYPE_CHECKING, Literal

from sqlalchemy import UniqueConstraint, ForeignKey, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from .user import User
    from .book import Book

Status = Literal["to_read", "read"]


class BookStatus(Enum):
    TO_READ: str = "to_read"
    READ: str = "read"


class UserBookAssociation(Base):
    __table_args__ = (
        UniqueConstraint(
            "user_id",
            "book_id",
            name="idx_unique_user_book",
        ),
    )

    book_id: Mapped[int] = mapped_column(
        ForeignKey(
            "books.id",
            ondelete="CASCADE",
        )
    )
    user_id: Mapped[int] = mapped_column(
        ForeignKey(
            "users.id",
            ondelete="CASCADE",
        )
    )
    rating: Mapped[float] = mapped_column(
        Float,
        default=0,
        server_default="0",
    )
    status: Mapped[Status]

    book: Mapped["Book"] = relationship(
        back_populates="users_details",
    )
    user: Mapped["User"] = relationship(
        back_populates="books_details",
    )
