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