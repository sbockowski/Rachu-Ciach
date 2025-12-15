from typing import Type, Any, Dict
from sqlalchemy import update
from sqlalchemy.orm import Session
from sqlalchemy.orm import DeclarativeBase

def update_row(session: Session, model: Type[DeclarativeBase], data: Dict[str,Any], updated_row_id: int):
    stmt= (
        update(model)
        .where(model.id == updated_row_id)
        .values(**data)
        )

    result = session.execute(stmt)
    session.commit()

    return result