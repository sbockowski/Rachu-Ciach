from db.utils.upsert import upsert
from .base_service import BaseService
from db.models import SavingsPlan, Goal, Budget

class SavingsPlanService(BaseService):
    def add_or_update_savings_plan(self, budget_id: int, goal_id: int, amount: float) -> int:
        session = self.Session()
        try:
            data = {
                "budget_id": budget_id, 
                "goal_id": goal_id, 
                "amount": amount
            }
            result = upsert(
                session=session,
                model=SavingsPlan,
                data=data,
                conflict_columns=["budget_id", "goal_id"]
            )

            inserted_pk = getattr(result, "inserted_primary_key", None)
            if inserted_pk[0] != 0:
                print("Add new savings plan.")
                return inserted_pk[0]

            # if UPDATE — get ID manually
            sp = (
                session.query(SavingsPlan)
                .filter(
                    SavingsPlan.budget_id == budget_id,
                    SavingsPlan.goal_id == goal_id
                )
                .first()
            )
            print("Update savings plan.")
            return sp.id
        finally:
            session.close()

    def get_planned_savings(self, budget_name: str):
        session = self.Session()
        try:
            q = (
                session.query(Budget.name, Goal.name, SavingsPlan.amount)
                .join(SavingsPlan, SavingsPlan.budget_id == Budget.id)
                .join(Goal, SavingsPlan.goal_id == Goal.id)
                .filter(Budget.name == budget_name)
            )
            results = q.all()
            return results
        finally:
            session.close()