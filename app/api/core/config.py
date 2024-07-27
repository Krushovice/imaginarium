from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    PROD_DB_URL: str
    ECHO: bool = True

    @property
    def get_db_url(self) -> str:
        return self.PROD_DB_URL

    model_config = SettingsConfigDict(env_file="../../../.env")


settings = Settings()
