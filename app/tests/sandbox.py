import asyncio

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.api.orm import User, UserBookAssociation, Book, db_helper


async def get_user_books(session: AsyncSession, username: str):
    stmt = (
        select(User)
        .options(
            selectinload(User.books_details).joinedload(UserBookAssociation.book),
        )
        .where(User.username == username)
    )
    user = await session.scalar(stmt)
    books = []
    for user_book_detail in user.books_details:
        books.append(user_book_detail.book)
    return list(books)


async def get_user_book_assoc(session: AsyncSession, username: str):
    stmt = (
        select(User)
        .options(
            selectinload(User.books_details).joinedload(UserBookAssociation.book),
        )
        .where(User.username == username)
    )
    user = await session.scalar(stmt)

    return user.books_details


new_book1 = Book(title="New Book", author="<NAME>", genre="horror")

new_book2 = Book(title="New Book2", author="<NAME2>", genre="adventure")


async def add_books_to_user(session: AsyncSession):
    user = await get_user_book_assoc(session=session, username="Krush")
    # Проверка, существует ли пользователь
    if user:
        # Создание ассоциаций и добавление их к пользователю

        user.books_details.append(
            UserBookAssociation(
                book=new_book1,
                rating=4,
                status="read",
            )
        )
        user.books_details.append(
            UserBookAssociation(
                book=new_book2,
                status="to_read",
            )
        )

        await session.commit()


async def main():
    async with db_helper.session_factory() as session:
        await add_books_to_user(session=session)


if __name__ == "__main__":
    asyncio.run(main())
