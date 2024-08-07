from typing import TYPE_CHECKING

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.engine import Result
from sqlalchemy.orm import selectinload


from app.api.orm import User, Profile


from .schemas import (
    UserCreate,
    UserUpdate,
    UserUpdatePartial,
    ProfileCreate,
    ProfileUpdate,
    ProfileUpdatePartial,
)


async def create_user(user_in: UserCreate, session: AsyncSession) -> User:
    user = User(**user_in.model_dump())
    session.add(user)
    await session.commit()
    # await session.refresh(book)
    return user


async def get_users(session: AsyncSession) -> list[User]:
    stmt = select(User).order_by(User.id)
    result: Result = await session.execute(stmt)
    users = result.scalars().all()
    return list(users)


async def get_user(user_id: int, session: AsyncSession) -> User | None:
    stmt = select(User).options(selectinload(User.profile)).filter(User.id == user_id)

    res: Result = await session.execute(stmt)
    user: User = res.scalar_one_or_none()
    return user


async def update_user(
    session: AsyncSession,
    user: User,
    user_update: UserUpdate | UserUpdatePartial,
    partial: bool = False,
) -> User:
    for name, value in user_update.model_dump(exclude_unset=partial).items():
        setattr(user, name, value)
    await session.commit()
    return user


async def create_user_profile(
    user_id: int,
    profile_in: ProfileCreate,
    session: AsyncSession,
) -> Profile:
    user = await get_user(user_id, session)
    user.profile = Profile(**profile_in.model_dump())

    await session.commit()
    return user.profile


async def update_user_profile(
    session: AsyncSession,
    profile: Profile,
    user_update: ProfileUpdate | ProfileUpdatePartial,
    partial: bool = False,
) -> Profile:
    for name, value in user_update.model_dump(exclude_unset=partial).items():
        setattr(profile, name, value)
    await session.commit()
    return profile


async def delete_user(
    session: AsyncSession,
    user: User,
) -> None:
    await session.delete(user)
