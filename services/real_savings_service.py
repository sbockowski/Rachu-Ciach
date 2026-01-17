from db.utils.update import update_row
from .base_service import BaseService
from db.models import RealSavings, Goal, Budget
from sqlalchemy.exc import IntegrityError

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

    def update_real_savings(self, budget_id: int, goal_id: int, amount: float, updated_row_id: int) -> int:
        session = self.Session()
        try:
            data = {
                "budget_id": budget_id, 
                "goal_id": goal_id, 
                "amount": amount
            }
            result = update_row(
                session=session,
                model=RealSavings,
                data=data,
                updated_row_id=updated_row_id
            )
            if result == True:
                print("Update real savings.")
                return updated_row_id
        finally:
            session.close()