from db.utils.update import update_row
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

    def change_goal_name(self, name: str, updated_row_id: int) -> int:
        session = self.Session()
        try:
            data = {
                "name": name
            }
            result = update_row(
                session=session,
                model=Goal,
                data=data,
                updated_row_id=updated_row_id
            )
            if result == True:
                print("Goal name updated.")
                return updated_row_id
        finally:
            session.close()