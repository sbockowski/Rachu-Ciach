from .base_service import BaseService
from db.models import RealIncome, Kind, Budget

class RealIncomeService(BaseService):
    def add_real_income(self, budget_id: int, kind_id: int, amount: float) -> int:
        session = self.Session()
        try:
            inc = RealIncome(budget_id = budget_id, kind_id = kind_id, amount = amount)
            session.add(inc)
            session.commit()
            session.refresh(inc)
            print("Add income.")
            return inc.id
        finally:
            session.close()

    def get_real_incomes(self, budget_name: str):
        session = self.Session()
        try:
            q = (
                session.query(Budget.name, Kind.name, RealIncome.amount)
                .join(RealIncome, RealIncome.budget_id == Budget.id)
                .join(Kind, RealIncome.kind_id == Kind.id)
                .filter(Budget.name == budget_name)
            )
            results = q.all()
            return results
        finally:
            session.close()