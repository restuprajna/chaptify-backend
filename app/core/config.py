import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    MONGO_DB_URL: str = os.getenv("MONGO_DB_URL", "mongodb://localhost:27017")
    DATABASE_NAME: str = "library_db"

settings = Settings()
