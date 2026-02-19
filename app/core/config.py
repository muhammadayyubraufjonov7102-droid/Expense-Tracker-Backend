from pydantic_settings import BaseSettings
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent.parent

class Settings(BaseSettings):
    DB_URL: str = "sqlite:///dev.db"
    
    model_config = {
        "env_file" : BASE_DIR / ".env"
    }
    
    
settings = Settings()