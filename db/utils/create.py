from typing import Type, Any, Dict
from sqlalchemy.orm import Session
from sqlalchemy.orm import DeclarativeBase

def create_row(session: Session, model: Type[DeclarativeBase], data: Dict[str,Any]) -> DeclarativeBase:
    obj = model(**data)
    session.add(obj)
    return obj