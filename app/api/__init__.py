from fastapi import APIRouter

from .core.users.user_handlers import router as user_router
from .core.books.book_handlers import router as book_router

router = APIRouter()
router.include_router(user_router, prefix="/users")
router.include_router(book_router, prefix="/books")
