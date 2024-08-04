from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path


BASE_DIR = Path(__file__).cwd()


class DbConfig(BaseModel):
    prod_url: str
    echo: bool = True
    dev_url: str


class Settings(BaseSettings):

    model_config = SettingsConfigDict(
        case_sensitive=False,
        env_file=".env",
    )

    db: DbConfig


settings = Settings()
