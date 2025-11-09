from db.connection import get_conn
from datetime import datetime

created_at = datetime.now().isoformat(timespec='seconds') # przerobić na funkcje


def create_budget(name: str):
    with get_conn() as conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO budget (name, created_at) VALUES (?, ?)",(name, created_at))
        conn.commit()
        return cur.lastrowid

def add_category(name: str) -> int:
    with get_conn() as conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO category (name) VALUES (?)", (name,))
        # category_id = cur.fetchone()[0]
        conn.commit()
        return cur.lastrowid

def add_income_type(name: str) -> int:
    with get_conn() as conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO income_type (name) VALUES (?)", (name,))
        # category_id = cur.fetchone()[0]
        conn.commit()
        return cur.lastrowid

def add_goal(name: str) -> int:
    with get_conn() as conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO goal (name) VALUES (?)", (name,))
        # category_id = cur.fetchone()[0]
        conn.commit()
        return cur.lastrowid


def add_income_plan(budget_id: int, type_id: int, amount: float):
    with get_conn() as conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO income_plan (budget_id, type_id, amount) VALUES (?, ?, ?)", (budget_id, type_id, amount))
        conn.commit()
        return cur.lastrowid

def add_spend_plan(budget_id: int, category_id: int, amount: float):
    with get_conn() as conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO spend_plan (budget_id, category_id, amount) VALUES (?, ?, ?)", (budget_id, category_id, amount))
        conn.commit()
        return cur.lastrowid

def add_savings_plan(budget_id: int, goal_id: int, amount: float):
    with get_conn() as conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO savings_plan (budget_id, goal_id, amount) VALUES (?, ?, ?)", (budget_id, goal_id, amount))
        conn.commit()
        return cur.lastrowid