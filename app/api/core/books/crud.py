from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.engine import Result


from .schemas import BookCreate
from api.orm import Book


async def create_book(book_in: BookCreate, session: AsyncSession) -> Book:
    book = Book(**book_in.model_dump())
    session.add(book)
    await session.commit()
    # await session.refresh(book)
    return book


async def get_books(session: AsyncSession) -> list[Book]:
    stmt = select(Book).order_by(Book.id)
    result: Result = await session.execute(stmt)
    books = result.scalars().all()
    return list(books)


async def get_book(book_id: int, session: AsyncSession) -> Book | None:
    return await session.get(Book, book_id)
