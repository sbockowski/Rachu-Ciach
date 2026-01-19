from db.models import Budget
from typing import Type, Any, Dict
from sqlalchemy.orm import Session
from sqlalchemy.orm import DeclarativeBase

def delete_row(session: Session, model: Type[DeclarativeBase], deleted_row_id: int, data: Dict[str,Any] | None = None):

    # check if deleted row exists
    record = session.get(model, deleted_row_id)
    if record is None:
        raise ValueError(f"Row {model.__tablename__} with id={deleted_row_id} does not exist")
    
    if data:
        # check if related budget exists
        if "budget_id" in data.keys():
            budget = session.get(Budget, data["budget_id"])
            if budget is None:
                raise ValueError(f"Budget with id={data["budget_id"]} does not exist")

    session.delete(record)
    return True