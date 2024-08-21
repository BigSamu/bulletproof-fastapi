from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from app.config.config import settings

# Engine for a MySQL Database
# engine = create_engine(settings.SQLALCHEMY_DATABASE_URI, pool_pre_ping=True)

# Engine for a SQLite Database
engine = create_engine(
    settings.SQLALCHEMY_DATABASE_URI, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Base = declarative_base()
