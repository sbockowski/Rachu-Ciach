from .base_service import BaseService
from db.models import Budget
from datetime import datetime
from sqlalchemy.exc import IntegrityError

def _now_str():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

class BudgetService(BaseService):

    def create_budget(self, name: str) -> int:
        session = self.Session()
        try:
            budget = Budget(name=name, created_at=_now_str())
            session.add(budget)
            session.commit()
            session.refresh(budget)
            return budget.id
        except IntegrityError as e:
            session.rollback()
            raise ValueError(f"Budget '{name}' already exists.") from e
        finally:
            session.close()