from db.connection import get_conn
from datetime import datetime

created_at = datetime.now().isoformat(timespec='seconds')


def create_budget(name: str):
    with get_conn() as conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO budget (name, created_at) VALUES (?, ?)",(name, created_at))
        conn.commit()
        return cur.lastrowid

def add_category(name: str) -> int:
    with get_conn() as conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO category (name) VALUES (?) RETURNING id", (name,))
        category_id = cur.fetchone()[0]
        conn.commit()
        return category_id
