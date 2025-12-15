from db.utils.update import update_row
from .base_service import BaseService
from db.models import RealSpend, Category, Budget

class RealSpendService(BaseService):
    def add_real_spend(self, budget_id: int, category_id: int, amount: float) -> int:
        session = self.Session()
        try:
            sp = RealSpend(budget_id = budget_id, category_id = category_id, amount = amount)
            session.add(sp)
            session.commit()
            session.refresh(sp)
            print("Add spend.")
            return sp.id
        finally:
            session.close()

    def get_real_spends(self, budget_name: str):
        session = self.Session()
        try:
            q = (
                session.query(Budget.name, Category.name, RealSpend.amount)
                .join(RealSpend, RealSpend.budget_id == Budget.id)
                .join(Category, RealSpend.category_id == Category.id)
                .filter(Budget.name == budget_name)
            )
            results = q.all()
            return results
        finally:
            session.close()

    def update_real_spend(self, budget_id: int, category_id: int, amount: float, updated_row_id: int) -> int:
        session = self.Session()
        try:
            data = {
                "budget_id": budget_id, 
                "category_id": category_id, 
                "amount": amount
            }
            result = update_row(
                session=session,
                model=RealSpend,
                data=data,
                updated_row_id=updated_row_id
            )
            if result:
                print("Update real spend.")
                return updated_row_id
            else:
                return 0
        finally:
            session.close()