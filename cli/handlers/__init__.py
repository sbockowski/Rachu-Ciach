from .crud_factory import *
from db.models import *

DISPATCHER = {
    "create_budget": create_budget_handler,
    "create_goal": create_handler(
        model=Goal,
        msg_template="Created goal with name {data[name]}",
        fields=["name"]
    ),
    "create_category": create_handler(
        model=Category,
        msg_template="Created category with name {data[name]}",
        fields=["name"]
    ),
    "create_kind": create_handler(
        model=Kind,
        msg_template="Created kind with name {data[name]}",
        fields=["name"]
    ),
    "create_real_savings": create_handler(
        model=RealSavings,
        msg_template="Created real savings with ID {id}",
        fields=["budget_id", "goal_id", "amount"]
    ),
    "create_real_spends": create_handler(
        model=RealSpend,
        msg_template="Created real spend with ID {id}",
        fields=["budget_id", "category_id", "amount"]
    ),
    "create_real_incomes": create_handler(
        model=RealIncome,
        msg_template="Created real income with ID {id}",
        fields=["budget_id", "kind_id", "amount"]
    ),
    "update_real_savings": make_update_handler(
        model=RealSavings,
        msg_template="Updated real savings with ID {id}",
        fields=["budget_id", "goal_id", "amount"]
    ),
    "update_real_spends": make_update_handler(
        model=RealSpend,
        msg_template="Updated real spend with ID {id}",
        fields=["budget_id", "category_id", "amount"]
    ),
    "update_real_incomes": make_update_handler(
        model=RealIncome,
        msg_template="Updated real income with ID {id}",
        fields=["budget_id", "kind_id", "amount"]
    ),
    "set_plan_savings": set_plan_handler(
        model=SavingsPlan,
        msg_template="{operation_type} plan income with ID {pk}",
        classifier_field="goal_id",
        fields=["budget_id", "classifier_id", "amount"]
    ),
    "set_plan_spends": set_plan_handler(
        model=SpendPlan,
        msg_template="{operation_type} plan income with ID {pk}",
        classifier_field="category_id",
        fields=["budget_id", "classifier_id", "amount"]
    ),
    "set_plan_incomes": set_plan_handler(
        model=IncomePlan,
        msg_template="{operation_type} plan income with ID {pk}",
        classifier_field="kind_id",
        fields=["budget_id", "classifier_id", "amount"]
    ),
    "rename_goal": rename_classifier_handler(
        model=Goal,
        msg_template="Updated goal with ID {id}",
    ),
    "rename_category": rename_classifier_handler(
        model=Category,
        msg_template="Updated category with ID {id}",
    ),
    "rename_kind": rename_classifier_handler(
        model=Kind,
        msg_template="Updated kind with ID {id}",
    ),
    "delete_budget": delete_handler(
        model=Budget,
        msg_template="Deleted budget with ID {id} and all data related to it.",
        fields=["deleted_row_id"]
    ),
    "delete_goal": delete_handler(
        model=Goal,
        msg_template="Deleted goal with ID {id}",
        fields=["deleted_row_id"]
    ),
    "delete_category": delete_handler(
        model=Category,
        msg_template="Deleted category with ID {id}",
        fields=["deleted_row_id"]
    ),
    "delete_kind": delete_handler(
        model=Kind,
        msg_template="Deleted kind with ID {id}",
        fields=["deleted_row_id"]
    ),
    "delete_real_spend": delete_handler(
        model=RealSpend,
        msg_template="Deleted real spend with ID {id}",
        fields=["budget_id", "deleted_row_id"]
    ),
    "delete_real_income": delete_handler(
        model=RealIncome,
        msg_template="Deleted real income with ID {id}",
        fields=["budget_id", "deleted_row_id"]
    ),
    "delete_real_saving": delete_handler(
        model=RealSavings,
        msg_template="Deleted real saving with ID {id}",
        fields=["budget_id", "deleted_row_id"]
    ),
    "delete_spend_plan": delete_handler(
        model=SpendPlan,
        msg_template="Deleted spend plan with ID {id}",
        fields=["budget_id", "deleted_row_id"]
    ),
    "delete_income_plan": delete_handler(
        model=IncomePlan,
        msg_template="Deleted income plan with ID {id}",
        fields=["budget_id", "deleted_row_id"]
    ),
    "delete_savings_plan": delete_handler(
        model=SavingsPlan,
        msg_template="Deleted savings plan with ID {id}",
        fields=["budget_id", "deleted_row_id"]
    ),
    "show_goals": show_table_handler(
        model=Goal
    )
}