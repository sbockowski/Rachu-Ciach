from db.session import SessionLocal


def get_name_by_id(model, model_id):
    session = SessionLocal()
    try:
        result = (session.query(model.name).filter(model.id == model_id).one_or_none())
        if result is None:
            return None
        return result[0]
    finally:
        session.close()