from .base_service import BaseService
from db.models import RealSavings, Goal, Budget

class RealSavingsService(BaseService):
    def add_real_savings(self, budget_id: int, goal_id: int, amount: float) -> int:
        session = self.Session()
        try:
            sp = RealSavings(budget_id = budget_id, goal_id = goal_id, amount = amount)
            session.add(sp)
            session.commit()
            session.refresh(sp)
            print("Add saving.")
            return sp.id
        finally:
            session.close()

    def get_real_savings(self, budget_name: str):
        session = self.Session()
        try:
            q = (
                session.query(Budget.name, Goal.name, RealSavings.amount)
                .join(RealSavings, RealSavings.budget_id == Budget.id)
                .join(Goal, RealSavings.goal_id == Goal.id)
                .filter(Budget.name == budget_name)
            )
            results = q.all()
            return results
        finally:
            session.close()