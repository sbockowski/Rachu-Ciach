

def row_to_dict(row) -> dict:
    return {
        col.name: getattr(row, col.name)
        for col in row.__table__.columns
    }