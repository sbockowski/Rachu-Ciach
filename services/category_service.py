from db.utils.update import update_row
from .base_service import BaseService
from db.models import Category
from sqlalchemy.exc import IntegrityError

class CategoryService(BaseService):

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

    def change_category_name(self, name: str, updated_row_id: int) -> int:
        session = self.Session()
        try:
            data = {
                "name": name
            }
            result = update_row(
                session=session,
                model=Category,
                data=data,
                updated_row_id=updated_row_id
            )
            if result == True:
                print("Category name updated.")
                return updated_row_id
        finally:
            session.close()