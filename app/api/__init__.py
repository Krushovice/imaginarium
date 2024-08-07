from fastapi import APIRouter

from .core.users.views import router as user_router
from .core.books.views import router as book_router
from .core.profiles.views import router as profile_router

router = APIRouter()
router.include_router(user_router, prefix="/users")
router.include_router(book_router, prefix="/books")
router.include_router(book_router, prefix="/profile")
