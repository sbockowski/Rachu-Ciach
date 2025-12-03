# services/budget_service.py
from services.upsert import upsert
from db.models import Budget, Category, Kind, Goal, SpendPlan, IncomePlan, SavingsPlan
from db.session import SessionLocal
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
            session.commit()
            session.refresh(kind)
            return kind.id
        except IntegrityError as e:
            session.rollback()
            raise ValueError(f"Kind '{name}' already exists.") from e
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
            if inserted_pk:
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

    def add_or_update_income_plan(self, budget_id: int, kind_id: int, amount: float) -> int:
        session = self.Session()
        try:
            data = {
                "budget_id": budget_id, 
                "kind_id": kind_id, 
                "amount": amount
            }
            result = upsert(
                session=session,
                model=IncomePlan,
                data=data,
                conflict_columns=["budget_id", "kind_id"]
            )

            inserted_pk = getattr(result, "inserted_primary_key", None)
            if inserted_pk:
                print("Add new income plan.")
                return inserted_pk[0]

            # if UPDATE — get ID manually
            ip = (
                session.query(IncomePlan)
                .filter(
                    IncomePlan.budget_id == budget_id,
                    IncomePlan.kind_id == kind_id
                )
                .first()
            )
            print("Update income plan.")
            return ip.id
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

    def get_category_list(self):
        session = self.Session()
        try:
            q = (
                session.query(Category.id, Category.name)
            )
            results = q.all()
            return results
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