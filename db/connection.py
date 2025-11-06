import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent.parent / "rachu-ciach.db"

def get_conn():
    return sqlite3.connect(DB_PATH)

def init_db():
    schema = """
    DROP TABLE IF EXISTS budget;
    DROP TABLE IF EXISTS income_plan;
    DROP TABLE IF EXISTS spend_plan;
    DROP TABLE IF EXISTS savings_plan;
    DROP TABLE IF EXISTS real_income;
    DROP TABLE IF EXISTS real_spend;
    DROP TABLE IF EXISTS real_savings;
    DROP TABLE IF EXISTS category;
    DROP TABLE IF EXISTS goal;
    DROP TABLE IF EXISTS income_type;


    PRAGMA foreign_keys=ON;

    CREATE TABLE IF NOT EXISTS budget(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE,
        created_at TEXT NOT NULL
    );

    CREATE TABLE IF NOT EXISTS category(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE
    );

    CREATE TABLE IF NOT EXISTS goal(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE
    );

    CREATE TABLE IF NOT EXISTS income_type(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE
    );

    CREATE TABLE IF NOT EXISTS income_plan(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        budget_id INT NOT NULL,
        type_id INT NOT NULL,
        amount REAL NOT NULL,
        FOREIGN KEY (budget_id) REFERENCES budget(id),
        FOREIGN KEY (type_id) REFERENCES type(id)
    );

    CREATE TABLE IF NOT EXISTS spend_plan(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        budget_id INT NOT NULL,
        category_id INT NOT NULL,
        amount REAL NOT NULL,
        FOREIGN KEY (budget_id) REFERENCES budget(id),
        FOREIGN KEY (category_id) REFERENCES category(id)
    );

    CREATE TABLE IF NOT EXISTS savings_plan(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        budget_id INT NOT NULL,
        goal_id INT NOT NULL,
        amount REAL NOT NULL,
        FOREIGN KEY (budget_id) REFERENCES budget(id),
        FOREIGN KEY (goal_id) REFERENCES goal(id)
    );

    CREATE TABLE IF NOT EXISTS real_income(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        budget_id INT NOT NULL,
        type_id INT NOT NULL,
        amount REAL NOT NULL,
        FOREIGN KEY (budget_id) REFERENCES budget(id),
        FOREIGN KEY (type_id) REFERENCES type(id)
    );

    CREATE TABLE IF NOT EXISTS real_spend(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        budget_id INT NOT NULL,
        category_id INT NOT NULL,
        amount REAL NOT NULL,
        FOREIGN KEY (budget_id) REFERENCES budget(id),
        FOREIGN KEY (category_id) REFERENCES category(id)
    );

    CREATE TABLE IF NOT EXISTS real_savings(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        budget_id INT NOT NULL,
        goal_id INT NOT NULL,
        amount REAL NOT NULL,
        FOREIGN KEY (budget_id) REFERENCES budget(id),
        FOREIGN KEY (goal_id) REFERENCES goal(id)
    );
    """

    with get_conn() as conn:
        conn.executescript(schema)
        conn.commit()