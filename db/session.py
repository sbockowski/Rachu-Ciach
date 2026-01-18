import sqlite3
from sqlalchemy import create_engine, event
from sqlalchemy.engine import Engine
from sqlalchemy.orm import sessionmaker


SQLITE_PATH = "sqlite:///db/rachu-ciach.db"

engine = create_engine(
    SQLITE_PATH,
    connect_args={"check_same_thread": False},
    future=True,
)

@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    if isinstance(dbapi_connection, sqlite3.Connection):
        cursor = dbapi_connection.cursor()
        cursor.execute("PRAGMA foreign_keys=ON")
        cursor.close()
        
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False, future=True)
