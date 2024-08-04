from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column


from .base import Base


class Book(Base):

    title: Mapped[str] = mapped_column(String(50))
    author: Mapped[str] = mapped_column(String(50))
    genre: Mapped[str] = mapped_column(String(20))

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id!r}, title={self.title!r})"

    def __repr__(self) -> str:
        return str(self)
