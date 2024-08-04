import asyncio

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.orm import db_helper, User, Profile, Review


async def create_user(
    session: AsyncSession,
    username: str,
    email: str,
) -> User:
    user = User(
        username=username,
        email=email,
    )
    session.add(user)
    await session.commit()
    print("user", user)
    return user


async def get_user_by_username(
    session: AsyncSession,
    username: str,
) -> User | None:
    stmt = select(User).where(User.username == username)
    user: User | None = await session.scalar(stmt)
    print("user", user)
    return user


async def main():
    async with db_helper.session_factory() as session:
        await create_user(
            session=session,
            username="Anna",
            email="Anna@yahoo.com",
        )
        await get_user_by_username(session=session, username="Krush")


if __name__ == "__main__":
    asyncio.run(main())
