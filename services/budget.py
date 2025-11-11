from db.connection import get_conn
from datetime import datetime
import sqlite3

def _now_str():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def create_budget(name: str):
    with get_conn() as conn:
        cur = conn.cursor()
        created_at = _now_str()
        cur.execute("INSERT INTO budget (name, created_at) VALUES (?, ?)",(name, created_at))
        conn.commit()
        return cur.lastrowid

def add_category(name: str) -> int:
    with get_conn() as conn:
        cur = conn.cursor()
        try:
            cur.execute("INSERT INTO category (name) VALUES (?)", (name,))
            conn.commit()
            return cur.lastrowid
        except sqlite3.IntegrityError as e:
            raise ValueError(f"Category '{name}' already exists.") from e

def add_income_type(name: str) -> int:
    with get_conn() as conn:
        cur = conn.cursor()
        try:
            cur.execute("INSERT INTO income_type (name) VALUES (?)", (name,))
            conn.commit()
            return cur.lastrowid
        except sqlite3.IntegrityError as e:
            raise ValueError(f"Income type '{name}' already exists.") from e


def add_goal(name: str) -> int:
    with get_conn() as conn:
        cur = conn.cursor()
        try:
            cur.execute("INSERT INTO goal (name) VALUES (?)", (name,))
            conn.commit()
            return cur.lastrowid
        except sqlite3.IntegrityError as e:
            raise ValueError(f"Goal '{name}' already exists.") from e



def add_income_plan(budget_id: int, type_id: int, amount: float) -> int:
    with get_conn() as conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO income_plan (budget_id, type_id, amount) VALUES (?, ?, ?)", (budget_id, type_id, amount))
        conn.commit()
        return cur.lastrowid

def add_spend_plan(budget_id: int, category_id: int, amount: float) -> int:
    with get_conn() as conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO spend_plan (budget_id, category_id, amount) VALUES (?, ?, ?)", (budget_id, category_id, amount))
        conn.commit()
        return cur.lastrowid

def add_savings_plan(budget_id: int, goal_id: int, amount: float) -> int:
    with get_conn() as conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO savings_plan (budget_id, goal_id, amount) VALUES (?, ?, ?)", (budget_id, goal_id, amount))
        conn.commit()
        return cur.lastrowid