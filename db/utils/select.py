from typing import Type
from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.orm import DeclarativeBase

def get_table(session: Session, model: Type[DeclarativeBase], budget_id: int | None = None):
    if budget_id is not None:
        if not getattr(model, "supports_budget_filter", False):
            raise ValueError(
                f"Model '{model.__name__}' does not support filtering by budget_id"
            )
        stmt = select(model).where(model.budget_id == budget_id)
    else:
        stmt = select(model)
    return session.scalars(stmt).all()

def get_name_by_id(session: Session, model: Type[DeclarativeBase], model_id):
    try:
        result = session.get(model, model_id)
        return result.name
    except Exception as e:
        raise ValueError(f"{model.__tablename__.capitalize()} with id={model_id} does not exist.") from e
    finally:
        session.close()