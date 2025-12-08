import argparse
from db.utils.select import get_name_by_id
from db.session import engine
from services import (BudgetService, CategoryService, KindService, GoalService, SpendPlanService, 
    IncomePlanService, SavingsPlanService)
from db.models import (Base, Budget, Kind, Category, Goal, SpendPlan, IncomePlan, SavingsPlan)

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

    # add-kind
    parser_add_kind = subparsers.add_parser("add-kind", help="Add a new income kind")
    parser_add_kind.add_argument("name", type=str, help="Income kind name")

    # add-goal
    parser_add_goal = subparsers.add_parser("add-goal", help="Add a new goal")
    parser_add_goal.add_argument("name", type=str, help="Goal type name")

    # add-income-plan
    parser_add_income_plan = subparsers.add_parser("add-or-update-income-plan", help="Add a new income plan")
    parser_add_income_plan.add_argument("budget_id", type=int, help="Budget id")
    parser_add_income_plan.add_argument("kind_id", type=int, help="Income kind id")
    parser_add_income_plan.add_argument("amount", type=float, help="Amount of income")

    # add-spend-plan
    parser_add_spend_plan = subparsers.add_parser("add-or-update-spend-plan", help="Add a new spend plan")
    parser_add_spend_plan.add_argument("budget_id", type=int, help="Budget id")
    parser_add_spend_plan.add_argument("category_id", type=int, help="Category id")
    parser_add_spend_plan.add_argument("amount", type=float, help="Amount of spend")

    # add-savings-plan
    parser_add_savings_plan = subparsers.add_parser("add-or-update-savings-plan", help="Add a new savings plan")
    parser_add_savings_plan.add_argument("budget_id", type=int, help="Budget id")
    parser_add_savings_plan.add_argument("goal_id", type=int, help="Goal id")
    parser_add_savings_plan.add_argument("amount", type=float, help="Amount of savings")

    parser_get_plan_spends = subparsers.add_parser("show-planned-spends")
    parser_get_plan_spends.add_argument("budget_name", type=str, help="Show planned spends with givin budget name")

    parser_get_plan_savings = subparsers.add_parser("show-planned-savings")
    parser_get_plan_savings.add_argument("budget_name", type=str, help="Show planned savings with givin budget name")

    parser_get_goals = subparsers.add_parser("show-goals", help="Show list of goals")

    parser_get_kinds = subparsers.add_parser("show-kinds", help="Show list of kinds")
    
    parser_get_categories = subparsers.add_parser("show-categories", help="Show list of categories")

    parser_get_name_by_id = subparsers.add_parser("get-name-by-id")
    parser_get_name_by_id.add_argument("model", type=str)
    parser_get_name_by_id.add_argument("model_id", type=int)

    args = parser.parse_args()


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
        Base.metadata.create_all(bind=engine)
        print("DB tables created (if not present).")

    elif args.cmd == "create-budget":
        budget_service = BudgetService()
        budget_id = budget_service.create_budget(args.name)
        print(f"Budget '{args.name}' created with id={budget_id}")

    elif args.cmd == "add-category":
        category_service = CategoryService()
        category_id = category_service.add_category(args.name)
        print(f"Category '{args.name}' created with id={category_id}")

    elif args.cmd == "add-kind":
        kind_service = KindService()
        kind_id = kind_service.add_kind(args.name)
        print(f"Income kind '{args.name}' created with id={kind_id}")

    elif args.cmd == "add-goal":
        goal_service = GoalService()
        goal_id = goal_service.add_goal(args.name)
        print(f"Goal '{args.name}' created with id={goal_id}")

    elif args.cmd == "add-or-update-income-plan":
        income_plan_service = IncomePlanService()
        income_plan_id = income_plan_service.add_or_update_income_plan(args.budget_id, args.kind_id, args.amount)
        kind_name = get_name_by_id(Kind, args.kind_id)
        print(f"Savings plan id: {income_plan_id}")
        print(f"Goal: {kind_name}")
        print(f"Amount: {args.amount}")

    elif args.cmd == "add-or-update-spend-plan":
        spend_plan_service = SpendPlanService()
        spend_plan_id = spend_plan_service.add_or_update_spend_plan(args.budget_id, args.category_id, args.amount)
        category_name = get_name_by_id(Category, args.category_id)
        print(f"Savings plan id: {spend_plan_id}")
        print(f"Goal: {category_name}")
        print(f"Amount: {args.amount}")

    elif args.cmd == "add-or-update-savings-plan":
        savings_plan_service = SavingsPlanService()
        savings_plan_id = savings_plan_service.add_or_update_savings_plan(args.budget_id, args.goal_id, args.amount)
        goal_name = get_name_by_id(Goal, args.goal_id)
        print(f"Savings plan id: {savings_plan_id}")
        print(f"Goal: {goal_name}")
        print(f"Amount: {args.amount}")

    elif args.cmd == "show-planned-spends":
        spend_plan_service = SpendPlanService()
        rows = spend_plan_service.get_planned_spends(args.budget_name)
        for bname, cname, amount in rows:
            print(f"{bname} | {cname} | {amount}")
    
    elif args.cmd == "show-planned-savings":
        savings_plan_service = SavingsPlanService()
        rows = savings_plan_service.get_planned_savings(args.budget_name)
        for bname, gname, amount in rows:
            print(f"{bname} | {gname} | {amount}")
    
    elif args.cmd == "show-goals":
        goal_service = GoalService()
        rows = goal_service.get_goal_list()
        for gid, gname in rows:
            print(f"{gid} | {gname}")

    elif args.cmd == "show-kinds":
        kind_service = KindService()
        rows = kind_service.get_kind_list()
        for kid, kname in rows:
            print(f"{kid} | {kname}")

    elif args.cmd == "show-categories":
        category_service = CategoryService()
        rows = category_service.get_category_list()
        for cid, cname in rows:
            print(f"{cid} | {cname}")

    elif args.cmd == "get-name-by-id":
        row = get_name_by_id(args.model, args.model_id)
        print(row)

if __name__ == "__main__":
    main()
