from __future__ import annotations
from typing import List
from sqlalchemy import Integer, Float, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship, mapped_column, Mapped
from .base import Base

class IncomePlan(Base):
    __tablename__ = "income_plan"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    budget_id: Mapped[int] = mapped_column(ForeignKey("budget.id"), nullable=False)
    type_id: Mapped[int] = mapped_column(ForeignKey("kind.id"), nullable=False)
    amount: Mapped[float] = mapped_column(Float, nullable=False)

    budget: Mapped["Budget"] = relationship("Budget", back_populates="income_plans")
    kind: Mapped["Kind"] = relationship("Kind", back_populates="income_plans")

    __table_args__ = (
        UniqueConstraint("budget_id", "kind_id", name="uix_income_plan"),
    )

class RealIncome(Base):
    __tablename__ = "real_income"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    budget_id: Mapped[int] = mapped_column(ForeignKey("budget.id"), nullable=False)
    type_id: Mapped[int] = mapped_column(ForeignKey("kind.id"), nullable=False)
    amount: Mapped[float] = mapped_column(Float, nullable=False)

    budget: Mapped["Budget"] = relationship("Budget", back_populates="real_incomes")
    kind: Mapped["Kind"] = relationship("Kind", back_populates="real_incomes")
