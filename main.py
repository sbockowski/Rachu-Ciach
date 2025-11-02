from db.connection import init_db
from services.budget import created_budget

def main():
    init_db()
    print("Budżet rachu-ciach")