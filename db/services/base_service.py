from typing import Any, Dict, Type

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import DeclarativeBase

from db.session import SessionLocal
from db.utils.create import create_row
from db.utils.delete import delete_row
from db.utils.select import get_table
from db.utils.update import update_row
from db.utils.upsert import upsert


class BaseService:
    def __init__(self):
        self.Session = SessionLocal

    def create(
        self, model: Type[DeclarativeBase], data: Dict[str, Any]
    ) -> DeclarativeBase:
        session = self.Session()
        try:
            result = create_row(
                session=session,
                model=model,
                data=data,
            )
            session.commit()
            session.refresh(result)
            return result
        # except IntegrityError as e:
        #     session.rollback()
        #     raise ValueError(f"Category '{name}' already exists.") from e
        finally:
            session.close()

    def show_table(
        self, model: Type[DeclarativeBase], budget_id: int | None = None, joins=None
    ):
        session = self.Session()
        try:
            result = get_table(
                session=session, model=model, budget_id=budget_id, joins=joins
            )
            return result
        finally:
            session.close()

    def set_plan(
        self,
        model: Type[DeclarativeBase],
        budget_id: int,
        classifier_field: str,
        classifier_id: int,
        amount: float,
    ) -> int:
        session = self.Session()
        try:
            filters = {
                "budget_id": budget_id,
                classifier_field: classifier_id,
            }

            exists = session.query(model.id).filter_by(**filters).first() is not None

            data = {
                "budget_id": budget_id,
                classifier_field: classifier_id,
                "amount": amount,
            }

            result = upsert(
                session=session,
                model=model,
                data=data,
                conflict_columns=["budget_id", classifier_field],
            )
            session.commit()

            return [result, "Updated"] if exists else [result, "Created"]

        finally:
            session.close()

    def update(
        self, model: Type[DeclarativeBase], updated_row_id: int, data: dict
    ) -> int:
        session = self.Session()
        try:
            result = update_row(
                session=session, model=model, data=data, updated_row_id=updated_row_id
            )
            session.commit()
            return updated_row_id
        finally:
            session.close()

    def rename_classifier(
        self, model: Type[DeclarativeBase], name: str, updated_row_id: int
    ) -> int:
        session = self.Session()
        data = {
            "name": name,
        }
        try:
            result = update_row(
                session=session, model=model, data=data, updated_row_id=updated_row_id
            )
            session.commit()
            if result:
                return updated_row_id
        except IntegrityError as e:
            session.rollback()
            raise ValueError(
                f"{model.__tablename__.capitalize()} '{name}' already exists."
            ) from e
        finally:
            session.close()

    def delete(
        self,
        model: Type[DeclarativeBase],
        deleted_row_id: int,
        data: Dict[str, Any] | None = None,
    ) -> int:
        session = self.Session()
        try:
            result = delete_row(
                session=session, model=model, deleted_row_id=deleted_row_id, data=data
            )
            session.commit()
            return result
        finally:
            session.close()
