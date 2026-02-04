from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache

class Settings(BaseSettings):
    """Application Settings"""
    
    # app
    app_name: str = 'BootCamp'
    app_version: str = '1.0.0'
    debug: bool = False
    
    # database
    database_url: str
    database_echo: bool = False
    
    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
        case_sensitive=False
    )
    
@lru_cache
def get_settings() -> Settings:
    """Get Cached Settings Instance"""
    return Settings()