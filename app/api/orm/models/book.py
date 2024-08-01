from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column


from .base import Base


class Book(Base):
    __tablename__ = "books"

    title: Mapped[str] = mapped_column(String(50))
    author: Mapped[str] = mapped_column(String(50))
    genre: Mapped[str] = mapped_column(String(20))

    def __repr__(self) -> str:
        return f"Book(id={self.id!r}, title={self.title!r}, author={self.author!r})"
