from pydantic_settings import BaseSettings
from pathlib import Path

class Settings(BaseSettings):
    database_url: str

    class Config:
        env_file = str(Path(__file__).parent.parent / ".env")
# type: ignore

