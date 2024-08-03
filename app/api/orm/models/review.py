from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column


from .base import Base


class Review(Base):

    title: Mapped[str] = mapped_column(String(50), unique=False)
    body: Mapped[str] = mapped_column(String(100))

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    def __repr__(self) -> str:
        return f"Review(id={self.id!r}, title={self.title!r}, user_id={self.user_id!r})"
