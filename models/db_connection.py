from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import Settings

# Use DATABASE_URL from config.py
settings = Settings() # type: ignore
SQLALCHEMY_DATABASE_URL = settings.database_url
engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_size=10, max_overflow=20)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency for FastAPI routes
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()