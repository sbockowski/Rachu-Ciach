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