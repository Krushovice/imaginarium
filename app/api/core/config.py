from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path


BASE_DIR = Path(__file__).parent.parent


class Settings(BaseSettings):
    PROD_DB_URL: str
    ECHO: bool = True
    DEV_DB_URL: str

    model_config = SettingsConfigDict(env_file=f"{BASE_DIR}.env")


settings = Settings()
