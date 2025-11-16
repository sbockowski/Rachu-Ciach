import argparse
from services.budget_service import BudgetService

def main():
    parser = argparse.ArgumentParser(
        description="Rachu Ciach - Budget manager CLI"
    )
    subparsers = parser.add_subparsers(dest="cmd", required=True)

    # init db
    subparsers.add_parser("init-db", help="Create all tables")

    # reset db
    parser_reset = subparsers.add_parser("reset-db", help="Reset DB (delete and create database)")
    parser_reset.add_argument("--yes", action="store_true", help="Confirm without prompt")
    
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
    svc = BudgetService()

    # dispatcher
    # if args.command == "init-db":
    #     print(init_db(reset=False))
    # elif args.command == "reset-db":
    #     if getattr(args, "yes", False):
    #         print(init_db(reset=True))
    #     else:
    #         confirm = input("⚠️ This function will delete all data. Enter 'yes' to confirm: ")
    #         if confirm.strip().lower() == "tak":
    #             print(init_db(reset=True))
    #         else:
    #             print("Database reset cancelled.")

    if args.cmd == "init-db":
        from db.session import engine
        from db.models.base import Base
        Base.metadata.create_all(bind=engine)
        print("DB tables created (if not present).")

    elif args.cmd == "create-budget":
        budget_id = create_budget(args.name)
        print(f"Budget '{args.name}' created with id={budget_id}")

    elif args.cmd == "add-category":
        category_id = add_category(args.name)
        print(f"Category '{args.name}' created with id={category_id}")

    elif args.cmd == "add-income-type":
        income_type_id = add_income_type(args.name)
        print(f"Income type '{args.name}' created with id={income_type_id}")

    elif args.cmd == "add-goal":
        goal_id = add_goal(args.name)
        print(f"Goal '{args.name}' created with id={goal_id}")

    elif args.cmd == "add-income-plan":
        # category_id = add_category(args.name)
        print(f"Add new entry for Income Plan. Set AMOUNT for income type NAME") # TODO - show amount and name

    elif args.cmd == "add-spend-plan":
        # category_id = add_category(args.name)
        print(f"Add new entry for Spend Plan. Set AMOUNT for category NAME") # TODO - show amount and name

    elif args.cmd == "add-savings-plan":
        # category_id = add_category(args.name)
        print(f"Add new entry for Savings Plan. Set AMOUT for goal NAME") # TODO - show amount and name


if __name__ == "__main__":
    main()

# main.py (fragment)
import argparse
from services.budget_service import BudgetService

def main():
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="cmd", required=True)

    sub.add_parser("init-db")
    parser_create = sub.add_parser("create-budget")
    parser_create.add_argument("name")

    parser_add_cat = sub.add_parser("add-category")
    parser_add_cat.add_argument("name")

    parser_get_plan = sub.add_parser("show-planned")
    parser_get_plan.add_argument("budget_name")

    args = parser.parse_args()
    svc = BudgetService()

    if args.cmd == "init-db":
        # utworzenie tabel (jeśli jeszcze nie istnieją)
        from db.session import Base, engine
        Base.metadata.create_all(bind=engine)
        print("DB tables created (if not present).")

    elif args.cmd == "create-budget":
        bid = svc.create_budget(args.name)
        print("Created budget id=", bid)

    elif args.cmd == "add-category":
        cid = svc.add_category(args.name)
        print("Category id=", cid)

    elif args.cmd == "show-planned":
        rows = svc.get_planned_spends(args.budget_name)
        for bname, cname, amount in rows:
            print(f"{bname} | {cname} | {amount}")
