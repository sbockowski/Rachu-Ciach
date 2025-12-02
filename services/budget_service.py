# services/budget_service.py
from db.session import SessionLocal
from db.models import Budget, Category, Kind, Goal, SpendPlan, IncomePlan, SavingsPlan
from datetime import datetime
from sqlalchemy.exc import IntegrityError

def _now_str():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

class BudgetService:
    def __init__(self):
        self.Session = SessionLocal

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

    def add_category(self, name: str) -> int:
        session = self.Session()
        try:
            cat = Category(name=name)
            session.add(cat)
            session.commit()
            session.refresh(cat)
            return cat.id
        except IntegrityError as e:
            session.rollback()
            raise ValueError(f"Category '{name}' already exists.") from e
        finally:
            session.close()

    def add_kind(self, name: str) -> int:
        session = self.Session()
        try:
            kind = Kind(name=name)
            session.add(kind)
            session.refresh(kind)
            return kind.id
        except IntegrityError as e:
            session.rollback()
            raise ValueError(f"Income type '{name}' already exists.") from e
        finally:
            session.close()

    def add_goal(self, name: str) -> int:
        session = self.Session()
        try:
            g = Goal(name=name)
            session.add(g)
            session.commit()
            session.refresh(g)
            return g.id
        except IntegrityError as e:
            session.rollback()
            raise ValueError(f"Goal '{name}' already exists.") from e
        finally:
            session.close()

    def add_spend_plan(self, budget_id: int, category_id: int, amount: float) -> int:
        session = self.Session()
        try:
            sp = SpendPlan(budget_id=budget_id, category_id=category_id, amount=amount)
            session.add(sp)
            session.commit()
            session.refresh(sp)
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

    def get_goal_list(self):
        session = self.Session()
        try:
            q = (
                session.query(Goal.id, Goal.name)
            )
            results = q.all()
            return results
        finally:
            session.close()