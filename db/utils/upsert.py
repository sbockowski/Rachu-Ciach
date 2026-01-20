from typing import Type, Any, Dict
from sqlalchemy.dialects.sqlite import insert
from sqlalchemy.orm import Session
from sqlalchemy.orm import DeclarativeBase

def upsert(session: Session, model: Type[DeclarativeBase], data: Dict[str,Any], conflict_columns: list[str]):
    stmt= (
        insert(model)
        .values(**data)
        .on_conflict_do_update(
            index_elements=[getattr(model, col) for col in conflict_columns], set_=data
        )
        .returning(model.id)
    )

    result = session.execute(stmt)
    row_id = result.scalar_one()
    return row_id