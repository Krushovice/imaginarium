from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path


BASE_DIR = Path(__file__).parent.parent.parent


class Settings(BaseSettings):
    PROD_DB_URL: str = "postrgresql+asyncpg://postgres:postgres@0.0.0.0:5432/postgres"
    ECHO: bool = True
    DEV_DB_URL: str = "sqlite+aiosqlite:///./db.sqlite3"

    # model_config = SettingsConfigDict(env_file=f"{BASE_DIR}.env")


settings = Settings()
