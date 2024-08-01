from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from .schemas import UserCreate, User

from . import crud

from api.orm import db_helper

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/", response_model=list(User))
async def get_users(
    session: AsyncSession = Depends(db_helper.session_dependency()),
):
    return await crud.get_user(session=session)


@router.get("/{user_id}", response_model=User)
async def get_book(
    user_id: int,
    session: AsyncSession = Depends(db_helper.session_dependency()),
):
    user = await crud.get_user(session=session, user_id=user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Book{user_id} not found!",
        )
    return user


@router.post("/create", response_model=User)
async def create_user(
    user_in: UserCreate,
    session: AsyncSession = Depends(
        db_helper.session_dependency(),
    ),
):
    return await crud.create_user(user_in=user_in, session=session)
