import pytest
import asyncio
import pytest_asyncio
from contextlib import nullcontext as does_not_raise

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload


from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.orm import db_helper, User, Base

from app.api.core.users import crud

#
# @pytest.fixture(scope="session", autouse=True)
# async def create_tables():
#     async with db_helper.engine.begin() as conn:
#         await conn.run_sync(Base.metadata.drop_all)
#         await conn.run_sync(Base.metadata.create_all)
#         yield
#         await conn.run_sync(Base.metadata.drop_all)
#
#
# @pytest.fixture(scope="session", autouse=True)
# def session():
#     session = AsyncSession(bind=db_helper.engine)
#     return session
#
# @pytest.mark.usefixtures("create_tables")
# class TestUserCrud:
#
#     @pytest.mark.parametrize(
#         "username, email, result, expectation",
#         [
#             ("AlexClare", "alex@mail.ru", User, does_not_raise()),
#             ("BobMarv", "bobby@yandex.ru", User, does_not_raise()),
#             ("", "", User, pytest.raises),
#         ],
#     )
#     @pytest.mark.asyncio
#     async def test_create(self, session):


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
        user = User(
            username="An",
            email="Anya@yahoo.com",
        )
        await crud.create_user(
            user_in=user,
            session=session,
        )
        # await get_user_by_username(session=session, username="Krush")


if __name__ == "__main__":
    asyncio.run(main())
