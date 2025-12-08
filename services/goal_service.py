from .base_service import BaseService
from db.models import Goal
from sqlalchemy.exc import IntegrityError


class GoalService(BaseService):
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