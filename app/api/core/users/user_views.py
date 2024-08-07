from fastapi import APIRouter, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from .schemas import (
    UserCreate,
    User,
    UserUpdate,
    UserUpdatePartial,
    Profile,
    ProfileCreate,
    ProfileUpdate,
    ProfileUpdatePartial,
)

from . import crud

from .dependencies import user_by_id

from app.api.orm import db_helper

router = APIRouter(tags=["users"])


@router.get("/", response_model=list[User])
async def get_users(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.get_users(session=session)


@router.get("/{user_id}/", response_model=User)
async def get_user(
    user: User = Depends(user_by_id),
) -> User:

    return user


@router.post(
    "/create/",
    response_model=User,
    status_code=status.HTTP_201_CREATED,
)
async def create_user(
    user_in: UserCreate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.create_user(user_in=user_in, session=session)


@router.put("/{user_id}/")
async def update_user(
    user_update: UserUpdate,
    user: User = Depends(user_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.update_user(
        session=session,
        user=user,
        user_update=user_update,
    )


@router.patch("/{user_id}/", response_model=User)
async def update_user_partial(
    user_update: UserUpdatePartial,
    user: User = Depends(user_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.update_user(
        session=session,
        user=user,
        user_update=user_update,
        partial=True,
    )


@router.delete(
    "/{user_id}/",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_user(
    user: User = Depends(user_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    await crud.delete_user(session=session, user=user)


@router.post(
    "/{user_id}/create_profile",
    response_model=Profile,
    status_code=status.HTTP_201_CREATED,
)
async def create_profile(
    profile_in: ProfileCreate,
    user: User = Depends(user_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> Profile:
    return await crud.create_user_profile(
        user_id=user.id,
        session=session,
        profile_in=profile_in,
    )


@router.get("/{user_id}/profile", response_model=Profile)
async def get_user_profile(
    user: User = Depends(user_by_id),
) -> Profile:

    return user.profile


@router.post(
    "/{user_id}/update_profile",
    response_model=Profile,
)
async def update_user_profile(
    profile_update: ProfileUpdatePartial,
    user: User = Depends(user_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.update_user_profile(
        session=session,
        profile=user.profile,
        user_update=profile_update,
        partial=True,
    )
