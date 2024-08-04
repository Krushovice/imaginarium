from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path


BASE_DIR = Path(__file__).cwd().parent


class DbConfig(BaseModel):
    url: str = f"sqlite+aiosqlite:///{BASE_DIR}/db.sqlite3"
    echo: bool = True


class Settings(BaseSettings):

    # model_config = SettingsConfigDict(
    #     case_sensitive=False,
    #     env_file="./.env",
    # )

    db: DbConfig = DbConfig()


settings = Settings()
