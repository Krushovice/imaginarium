from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.engine import Result
from sqlalchemy.orm import selectinload


from app.api.orm import Profile


async def create_user_profile(
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


async def get_user_profile(user_id: int, session: AsyncSession):
    user = await crud.get_user(user_id, session)
    return user.profile


async def delete_user_profile(
    session: AsyncSession,
    profile: Profile,
) -> None:
    await session.delete(profile)
