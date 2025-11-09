import argparse
from db.connection import init_db
from services.budget import *

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

    # add-income-type
    parser_add_income_type = subparsers.add_parser("add-income-type", help="Add a new income type")
    parser_add_income_type.add_argument("name", type=str, help="Income type name")

    # add-goal
    parser_add_goal = subparsers.add_parser("add-goal", help="Add a new goal")
    parser_add_goal.add_argument("name", type=str, help="Goal type name")

    # add-income-plan
    parser_add_income_plan = subparsers.add_parser("add-income-plan", help="Add a new income plan")
    parser_add_income_plan.add_argument("budget_id", type=int, help="Budget id")
    parser_add_income_plan.add_argument("income_type_id", type=int, help="Income type id")
    parser_add_income_plan.add_argument("amount", type=float, help="Amount of income")

    # add-spend-plan
    parser_add_spend_plan = subparsers.add_parser("add-spend-plan", help="Add a new spend plan")
    parser_add_spend_plan.add_argument("budget_id", type=int, help="Budget id")
    parser_add_spend_plan.add_argument("category_id", type=int, help="Category id")
    parser_add_spend_plan.add_argument("amount", type=float, help="Amount of spend")

    # add-savings-plan
    parser_add_savings_plan = subparsers.add_parser("add-savings-plan", help="Add a new savings plan")
    parser_add_savings_plan.add_argument("budget_id", type=int, help="Budget id")
    parser_add_savings_plan.add_argument("goal_id", type=int, help="Goal id")
    parser_add_savings_plan.add_argument("amount", type=float, help="Amount of savings")

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

    elif args.command == "add-income-type":
        income_type_id = add_income_type(args.name)
        print(f"Income type '{args.name}' created with id={income_type_id}")

    elif args.command == "add-goal":
        goal_id = add_goal(args.name)
        print(f"Goal '{args.name}' created with id={goal_id}")

    elif args.command == "add-income-plan":
        # category_id = add_category(args.name)
        print(f"Add new entry for Income Plan. Set AMOUNT for income type NAME") # TODO - show amount and name

    elif args.command == "add-spend-plan":
        # category_id = add_category(args.name)
        print(f"Add new entry for Spend Plan. Set AMOUNT for category NAME") # TODO - show amount and name

    elif args.command == "add-savings-plan":
        # category_id = add_category(args.name)
        print(f"Add new entry for Savings Plan. Set AMOUT for goal NAME") # TODO - show amount and name


if __name__ == "__main__":
    main()