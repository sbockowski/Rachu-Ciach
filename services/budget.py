from db.connection import get_conn

def created_budget(name: str):
    with get_conn() as conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO budget (name) VALUES (?)",(name,))
        conn.commit()
        return cur.lastrowid
