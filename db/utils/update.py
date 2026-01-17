# from db.models import Budget
from typing import Type, Any, Dict
from sqlalchemy import update
from sqlalchemy.orm import Session
from sqlalchemy.orm import DeclarativeBase

def update_row(session: Session, model: Type[DeclarativeBase], data: Dict[str,Any], updated_row_id: int):

    # check if updated row exists
    record = session.get(model, updated_row_id)
    if record is None:
        raise ValueError(f"Row {model.__tablename__} with id={updated_row_id} does not exist")

    # # check if realted budget exists
    # budget = session.get(Budget, data["budget_id"])
    # if budget is None:
    #     raise ValueError(f"Budget with id={data["budget_id"]} does not exist")

    for key, value in data.items():
        setattr(record, key, value)

    session.commit()

    return True