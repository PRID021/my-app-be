from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache


class Settings(BaseSettings):
    """
    Settings for the application.

    Reads configuration from a .env file.
    """
    DATABASE_URL: str
    LOG_LEVEL: str = "INFO"

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding='utf-8')


@lru_cache
def get_settings() -> Settings:
    """
    Get the application settings.

    Uses lru_cache to cache the settings object.
    """
    return Settings()

settings = get_settings()
