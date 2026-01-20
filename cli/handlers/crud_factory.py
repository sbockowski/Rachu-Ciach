from tabulate import tabulate
from db.models import Budget
from db.services.base_service import BaseService
from db.utils.orm import row_to_dict
from datetime import datetime

service = BaseService()

def create_handler(model, msg_template: str, fields: list[str]):
    """
    for create real_*:
        fields = ["budget_id", "classifier_id", "amount"]
        args   = [budget_id, classifier_id, amount]

    for create classifier:
        fields = ["name"]
        args   = [name]
    """
    def handler(*args):
        data = dict(zip(fields, args))
        result = service.create(
            model=model,
            data=data
        )
        print(msg_template.format(id=result.id))
    return handler

def create_budget_handler(*args):
    """
    for create classifier:
        args   = [name]
    """
    fields = ["name"]
    data = dict(zip(fields, args))
    data["created_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    result = service.create(
        model=Budget,
        data=data
    )

    print(f"Created budget with ID {result.id}")

def make_update_handler(model, msg_template: str, fields: list[str]):
    """
    fields = ["budget_id", "classifier_id", "amount"]
    args   = [updated_row_id, budget_id, classifier_id, amount]
    """
    def handler(*args):
        updated_row_id = args[0]
        values = args[1:]
        data = dict(zip(fields, values))

        service.update(
            model=model, 
            updated_row_id=updated_row_id, 
            data=data
        )
        print(msg_template.format(id=updated_row_id))
    return handler

def rename_classifier_handler(model, msg_template: str):
    """
    args   = [updated_row_id, name]
    """
    def handler(*args):
        updated_row_id = args[0]
        name = args[1]

        service.rename_classifier(
            model=model, 
            name=name,
            updated_row_id=updated_row_id, 
        )
        print(msg_template.format(id=updated_row_id))
    return handler

def set_plan_handler(model, msg_template: str, classifier_field, fields: list[str]):
    """
    fields = ["budget_id", "classifier_field", "classifier_id", "amount"]
    args   = [budget_id, classifier_field, classifier_id, amount]
    """
    def handler(*args):
        data = dict(zip(fields, args))
        result = service.set_plan(
            model=model,
            budget_id=data["budget_id"],
            classifier_field=classifier_field,
            classifier_id=data["classifier_id"],
            amount=data["amount"]
        )
        print(msg_template.format(pk=result[0], operation_type=result[1]))
    return handler

def delete_handler(model, msg_template: str, fields: list[str]):
    """
    for delete real_* and *_plan:
        fields = ["budget_id", "deleted_row_id"]
        args   = [budget_id, deleted_row_id]

    for delete classifier and budget:
        fields = ["deleted_row_id"]
        args   = [deleted_row_id]
    """
    def handler(*args):
        data = dict(zip(fields, args))
        service.delete(
            model=model, 
            deleted_row_id=data["deleted_row_id"], 
            data=data
        )
        print(msg_template.format(id=data["deleted_row_id"]))
    return handler

def show_table_handler(model, joins=None):
    def handler(*args):
        budget_id = args[0] if args else None
        table = service.show_table(
            model=model,
            budget_id=budget_id,
            joins=joins
        )
        # rows = [row_to_dict(r) for r in table]
        rows = []
        for row in table:
            data = row_to_dict(row)
            if joins:
                for rel_name in joins:
                    rel_obj = getattr(row, rel_name.key)
                    if rel_obj is not None:
                        # dodajemy klucz relacji z "_name" lub innym formatem
                        data[f"{rel_name}_name"] = getattr(rel_obj, "name", str(rel_obj))
            rows.append(data)
        print(tabulate(rows, headers="keys", tablefmt="github"))
    return handler

