from db.utils.delete import delete_row
from db.utils.update import update_row
from db.utils.select import get_name_by_id
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
        except IntegrityError as e:
            session.rollback()
            raise ValueError(f"Goal '{name}' already exists.") from e
        finally:
            session.close()

    def delete_goal(self, deleted_row_id: int) -> int:
        session = self.Session()
        try:
            goal_name = get_name_by_id(Goal, deleted_row_id)
            print("costam")
            confirm = input(f"Are you sure you want to delete the goal named {goal_name}? (Yes/No) :")
            
            if confirm.upper() == "YES":
                result = delete_row(
                    session=session,
                    model=Goal,
                    deleted_row_id=deleted_row_id,
                )
                if result:
                    print(f"Goal {deleted_row_id} was deleted.")
                    return True
            elif confirm.upper() == "NO":
                print(f"Goal {deleted_row_id} wasn't deleted.")
                return True
            else:
                print("Please answer Yes or No.")
        finally:
            session.close()