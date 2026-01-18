from db.session import SessionLocal

class BaseService:
    def __init__(self):
        self.Session = SessionLocal