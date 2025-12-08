from db.utils.upsert import upsert
from .base_service import BaseService
from db.models import IncomePlan


class IncomePlanService(BaseService):
    def add_or_update_income_plan(self, budget_id: int, kind_id: int, amount: float) -> int:
        session = self.Session()
        try:
            data = {
                "budget_id": budget_id, 
                "kind_id": kind_id, 
                "amount": amount
            }
            result = upsert(
                session=session,
                model=IncomePlan,
                data=data,
                conflict_columns=["budget_id", "kind_id"]
            )

            inserted_pk = getattr(result, "inserted_primary_key", None)
            if inserted_pk[0] != 0:
                print("Add new income plan.")
                return inserted_pk[0]

            # if UPDATE — get ID manually
            ip = (
                session.query(IncomePlan)
                .filter(
                    IncomePlan.budget_id == budget_id,
                    IncomePlan.kind_id == kind_id
                )
                .first()
            )
            print("Update income plan.")
            return ip.id
        finally:
            session.close()