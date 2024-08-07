from typing import Any

from fastapi import APIRouter, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from . import crud


from app.api.orm import db_helper, Profile

router = APIRouter(tags=["profiles"])


# @router.post(
#     "/create/",
#     response_model=Profile,
#     status_code=status.HTTP_201_CREATED,
# )
# async def create_profile(
#     user_id: int,
#     first_name: str | None,
#     last_name: str | None,
#     favorite_genre: str | None,
#     session: AsyncSession = Depends(db_helper.scoped_session_dependency),
# ) -> Any:
#
#     return await crud.create_profile(
#         user_id=user_id,
#         session=session,
#         first_name=first_name,
#         last_name=last_name,
#         favorite_genre=favorite_genre,
#     )


@router.get("/{profile_id}/", response_model=None)
async def get_profile(
    profile_id: int,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):

    return await crud.get_profile(
        profile_id=profile_id,
        session=session,
    )


# @router.patch(
#     "/{profile_id}/update/",
#     response_model=Profile,
# )
# async def update_profile(
#     profile: Profile,
#     session: AsyncSession = Depends(db_helper.scoped_session_dependency),
# ):
#     return await crud.update_profile(
#         session=session,
#         profile=profile,
#     )


@router.delete(
    "/{profile_id}/",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_profile(
    profile: Profile,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> None:
    await crud.delete_profile(session=session, profile=profile)
