from .schemas import CreateBook


def create_book(book_in: CreateBook):
    book = book_in.model_dump()
    return {
        "message": "Book created!",
        "book": book,
    }
