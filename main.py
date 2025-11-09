import argparse
from db.connection import init_db
from services.budget import create_budget, add_category

def main():
    # init_db()
    # print("Budżet rachu-ciach!")
    # budget_name = input("Podaj nazwę budżetu: ")
    # budget_id = create_budget(budget_name)
    # print(f"Utworzono budżet id={budget_id},name={budget_name}")

    parser = argparse.ArgumentParser(
        description="Rachu Ciach - Budget manager CLI"
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # init db
    subparsers.add_parser("init-db", help="Create all tables")
    
    # create-budget
    parser_create_budget = subparsers.add_parser("create-budget", help="Create a new budget")
    parser_create_budget.add_argument("name", type=str, help="Budget name")


    # add-category
    parser_add_category = subparsers.add_parser("add-category", help="Add a new category")
    parser_add_category.add_argument("name", type=str, help="Category name")

    args = parser.parse_args()

    # dispatcher
    if args.command == "init-db":
        init_db()
        print("Database initialized")

    elif args.command == "create-budget":
        budget_id = create_budget(args.name)
        print(f"Budget '{args.name}' created with id={budget_id}")

    elif args.command == "add-category":
        category_id = add_category(args.name)
        print(f"Category '{args.name}' created with id={category_id}")

if __name__ == "__main__":
    main()