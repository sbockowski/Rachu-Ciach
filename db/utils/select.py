from db.session import SessionLocal


def get_name_by_id(model, model_id):
    session = SessionLocal()
    try:
        result = session.get(model, model_id)
        if result is None:
            return None
        return result.name
    finally:
        session.close()