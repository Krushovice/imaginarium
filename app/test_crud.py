import asyncio

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


async def main():
    async with db_helper.session_factory() as session:
        await create_user(
            session=session,
            username="Krush",
            email="krushovice@yahoo.com",
        )


if __name__ == "__main__":
    asyncio.run(main())
