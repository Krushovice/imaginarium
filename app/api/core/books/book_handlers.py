from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from .schemas import BookCreate, Book, BookUpdate, BookUpdatePartial

from api.orm import db_helper

from . import crud

from .dependencies import get_book_by_id

router = APIRouter(tags=["books"])


@router.get("/", response_model=list[Book])
async def get_books(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.get_books(session=session)


@router.get("/{book_id}/", response_model=Book)
async def get_book(
    book: Book = Depends(get_book_by_id),
):
    return book


@router.post(
    "/create/",
    response_model=Book,
    status_code=status.HTTP_201_CREATED,
)
async def create_book(
    book_in: BookCreate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.create_book(book_in=book_in, session=session)


@router.put("/{book_id}/")
async def update_book(
    book_update: BookUpdate,
    book: Book = Depends(get_book_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.update_book(
        session=session,
        book=book,
        book_update=book_update,
    )


@router.patch("/{book_id}/", response_model=Book)
async def update_book_partial(
    book_update: BookUpdatePartial,
    book: Book = Depends(get_book_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.update_book(
        session=session,
        book=book,
        book_update=book_update,
        partial=True,
    )


@router.delete(
    "/{book_id}/",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def update_book(
    book: Book = Depends(get_book_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    await crud.delete_book(session=session, book=book)
