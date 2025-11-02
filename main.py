from db.connection import init_db
from services.budget import create_budget

def main():
    init_db()
    print("Budżet rachu-ciach!")
    budget_name = input("Podaj nazwę budżetu: ")
    budget_id = create_budget(budget_name)
    print(f"Utworzono budżet id={budget_id},name={budget_name}")

if __name__ == "__main__":
    main()