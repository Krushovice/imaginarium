from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path


BASE_DIR = Path(__file__).parent.parent.parent
DB_PATH = BASE_DIR / "db.sqlite3"


class DbConfig(BaseModel):
    url: str = f"sqlite+aiosqlite:///{DB_PATH}"
    echo: bool = True


class Settings(BaseSettings):

    # model_config = SettingsConfigDict(
    #     case_sensitive=False,
    #     env_file="./.env",
    # )

    db: DbConfig = DbConfig()


settings = Settings()
