# db/session.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

SQLITE_PATH = "sqlite:///db/rachu-ciach.db"

engine = create_engine(
    SQLITE_PATH,
    connect_args={"check_same_thread": False},
    future=True,
)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False, future=True)
