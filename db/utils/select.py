from db.session import SessionLocal

def get_name_by_id(model, model_id):
    session = SessionLocal()
    try:
        result = session.get(model, model_id)
        return result.name
    except Exception as e:
        raise ValueError(f"{model.__tablename__.capitalize()} with id={model_id} does not exist.") from e
    finally:
        session.close()