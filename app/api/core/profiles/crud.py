from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.engine import Result


from app.api.orm import Profile


async def create_profile(
    session: AsyncSession,
    user_id: int,
    first_name: str | None,
    last_name: str | None,
    favorite_genre: str | None,
) -> Profile:

    profile = Profile(
        user_id=user_id,
        first_name=first_name,
        last_name=last_name,
        favorite_genre=favorite_genre,
    )

    session.add(profile)
    await session.commit()
    return profile


async def update_profile(
    session: AsyncSession,
    profile: Profile,
    **kwargs,
) -> Profile:
    for name, value in kwargs:
        setattr(profile, name, value)
    await session.commit()
    return profile


async def get_profile(profile_id: int, session: AsyncSession) -> Profile | None:
    stmt = select(Profile).where(Profile.id == profile_id)
    result: Result = await session.execute(stmt)
    profile: Profile | None = result.scalar_one_or_none()
    return profile


async def delete_profile(
    session: AsyncSession,
    profile: Profile,
) -> None:
    await session.delete(profile)
