from db.utils.update import update_row
from .base_service import BaseService
from db.models import Kind
from sqlalchemy.exc import IntegrityError

class KindService(BaseService):
    def add_kind(self, name: str) -> int:
        session = self.Session()
        try:
            kind = Kind(name=name)
            session.add(kind)
            session.commit()
            session.refresh(kind)
            return kind.id
        except IntegrityError as e:
            session.rollback()
            raise ValueError(f"Kind '{name}' already exists.") from e
        finally:
            session.close()

    def get_kind_list(self):
        session = self.Session()
        try:
            q = (
                session.query(Kind.id, Kind.name)
            )
            results = q.all()
            return results
        finally:
            session.close()

    def change_kind_name(self, name: str, updated_row_id: int) -> int:
        session = self.Session()
        try:
            data = {
                "name": name
            }
            result = update_row(
                session=session,
                model=Kind,
                data=data,
                updated_row_id=updated_row_id
            )
            if result == True:
                print("Kind name updated.")
                return updated_row_id
        except IntegrityError as e:
            session.rollback()
            raise ValueError(f"Kind '{name}' already exists.") from e
        finally:
            session.close()