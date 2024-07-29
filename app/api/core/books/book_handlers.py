from typing import Annotated

from fastapi import APIRouter, Path

from .schemas import CreateBook

from . import crud


router = APIRouter(prefix="/books", tags=["books"])


@router.get("/")
async def list_books():
    return [
        "Book1",
        "Book2",
        "Book3",
    ]


@router.get("/{book_id}")
async def read_book(book_id: Annotated[int, Path(ge=0)]):
    return {"book_id": book_id}


@router.post("/create")
def create_book(book: CreateBook):
    return crud.create_book(book_in=book)
