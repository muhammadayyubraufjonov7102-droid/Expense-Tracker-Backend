from pydantic_settings import BaseSettings
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent.parent

class Settings(BaseSettings):
    DB_URL: str = "sqlite:///dev.db"
    JWT_SECRET_KEY: str = "secret"
    JWT_ALGO: str = "HS256"
    
    model_config = {
        "env_file" : BASE_DIR / ".env"
    }
    
    
settings = Settings()