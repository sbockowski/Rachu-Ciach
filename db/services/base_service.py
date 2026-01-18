from typing import Type, Any, Dict
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.exc import IntegrityError
from db.session import SessionLocal
from db.utils.update import update_row
from db.utils.delete import delete_row
from db.utils.upsert import upsert

class BaseService:
    def __init__(self):
        self.Session = SessionLocal

    def set_plan(self, model: Type[DeclarativeBase], budget_id: int, classifier_id: int, amount: float) -> int:
        session = self.Session()
        try:
            exists = (
                session.query(model.id)
                .filter_by(
                    budget_id=budget_id,
                    classifier_id=classifier_id,
                )
                .first()
                is not None
            )

            data = {
                "budget_id": budget_id, 
                "classifier_id": classifier_id, 
                "amount": amount
            }

            upsert(
                session=session,
                model=model,
                data=data,
                conflict_columns=["budget_id", "classifier_id"]
            )

            return "updated" if exists else "created"

        finally:
            session.close()

    def update(self, model: Type[DeclarativeBase], updated_row_id: int, data: dict) -> int:
        session = self.Session()
        try:
            result = update_row(
                session=session,
                model=model,
                data=data,
                updated_row_id=updated_row_id
            )
            if result:
                return updated_row_id
        finally:
            session.close()

    def rename(self, model: Type[DeclarativeBase], name: str, updated_row_id: int) -> int:
        session = self.Session()
        data = {
            "name": name,
        }
        try:
            result = update_row(
                session=session,
                model=model,
                data=data,
                updated_row_id=updated_row_id
            )
            if result:
                return updated_row_id
        except IntegrityError as e:
            session.rollback()
            raise ValueError(f"{model.__tablename__.capitalize()} '{name}' already exists.") from e
        finally:
            session.close()