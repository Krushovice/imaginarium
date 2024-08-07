from fastapi import APIRouter, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from .schemas import (
    Profile,
    ProfileCreate,
    ProfileUpdate,
    ProfileUpdatePartial,
)

from . import crud

from app.api.core.users.dependencies import user_by_id

from app.api.orm import db_helper, User

router = APIRouter(tags=["profiles"])


@router.post(
    "/{profile_id}/create_profile",
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


@router.get("/{profile_id}/profile", response_model=Profile)
async def get_user_profile(
    user: User = Depends(user_by_id),
) -> Profile:

    return user.profile


@router.post(
    "/{profile_id}/update_profile",
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


@router.delete(
    "/{profile_id}/",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_user(
    user: User = Depends(user_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    await crud.delete_user_profile(session=session, profile=user.profile)
