from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column


from .base import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    first_name: Mapped[str] = mapped_column(String(50))
    last_name: Mapped[str] = mapped_column(String(50))
    username: Mapped[str] = mapped_column(
        String(50), unique=True, index=True, nullable=False
    )
    email: Mapped[str] = mapped_column(
        String(50), unique=True, index=True, nullable=False
    )

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.username!r}, fullname={self.first_name!r}{self.last_name!r})"
