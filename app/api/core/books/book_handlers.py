from fastapi import APIRouter, HTTPException, status

from .schemas import BookCreate, Book

from . import crud


router = APIRouter(prefix="/books", tags=["books"])


@router.get("/", response_model=list(Book))
async def get_books(session):
    return await crud.get_books(session=session)


@router.get("/{book_id}", response_model=Book)
async def get_book(book_id: int, session):
    book = await crud.get_book(session=session, book_id=book_id)
    if not book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Book{book_id} not found!",
        )
    return book


@router.post("/create", response_model=Book)
async def create_book(book_in: BookCreate, session):
    return await crud.create_book(book_in=book_in, session=session)
