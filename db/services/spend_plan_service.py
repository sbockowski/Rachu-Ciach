from db.utils.upsert import upsert
from .base_service import BaseService
from db.models import SpendPlan, Category, Budget    
    
class SpendPlanService(BaseService):   
    def add_or_update_spend_plan(self, budget_id: int, category_id: int, amount: float) -> int:
        session = self.Session()
        try:
            data = {
                "budget_id": budget_id, 
                "category_id": category_id, 
                "amount": amount
            }
            result = upsert(
                session=session,
                model=SpendPlan,
                data=data,
                conflict_columns=["budget_id", "category_id"]
            )

            inserted_pk = getattr(result, "inserted_primary_key", None)
            if inserted_pk[0] != 0:
                print("Add new spend plan.")
                return inserted_pk[0]

            # if UPDATE — get ID manually
            sp = (
                session.query(SpendPlan)
                .filter(
                    SpendPlan.budget_id == budget_id,
                    SpendPlan.category_id == category_id
                )
                .first()
            )
            print("Update spend plan.")
            return sp.id
        finally:
            session.close()

    def get_planned_spends(self, budget_name: str):
        session = self.Session()
        try:
            q = (
                session.query(Budget.name, Category.name, SpendPlan.amount)
                .join(SpendPlan, SpendPlan.budget_id == Budget.id)
                .join(Category, SpendPlan.category_id == Category.id)
                .filter(Budget.name == budget_name)
            )
            results = q.all()
            return results
        finally:
            session.close()