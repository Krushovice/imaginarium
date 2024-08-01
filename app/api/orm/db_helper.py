from sqlalchemy.ext.asyncio import (
    async_sessionmaker,
    create_async_engine,
    async_scoped_session,
    AsyncSession,
)
from asyncio import current_task
from api.core.config import settings


class DataBaseHelper:
    def __init__(self, url: str, echo: bool = False):
        self.engine = create_async_engine(
            url=url,
            echo=echo,
        )
        self.session_factory = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False,
        )

    # метод для получения актуальной сессии
    def get_scope_session(self):
        session = async_scoped_session(
            session_factory=self.session_factory,
            scopefunc=current_task,
        )
        return session

    # метод для создания сессии для каждого запроса и удаления ее после
    async def session_dependency(self) -> AsyncSession:
        async with self.get_scope_session() as session:
            yield session
            await session.remove()


db_helper = DataBaseHelper(
    url=settings.DEV_DB_URL,
    echo=settings.ECHO,
)
