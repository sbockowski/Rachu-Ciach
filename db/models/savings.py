from __future__ import annotations
from typing import List
from sqlalchemy import Integer, String, Float, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship, mapped_column, Mapped
from .base import Base

class SavingsPlan(Base):
    __tablename__ = "savings_plan"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    budget_id: Mapped[int] = mapped_column(ForeignKey("budget.id"), nullable=False)
    goal_id: Mapped[int] = mapped_column(ForeignKey("goal.id"), nullable=False)
    amount: Mapped[float] = mapped_column(Float, nullable=False)

    budget: Mapped["Budget"] = relationship("Budget")
    goal: Mapped["Goal"] = relationship("Goal", back_populates="savings_plans")

    supports_budget_filter = True # possible to filter by "budget_id"

    __table_args__ = (
        UniqueConstraint("budget_id", "goal_id", name="uix_savings_plan"),
    )

class RealSavings(Base):
    __tablename__ = "real_savings"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    budget_id: Mapped[int] = mapped_column(ForeignKey("budget.id"), nullable=False)
    goal_id: Mapped[int] = mapped_column(ForeignKey("goal.id"), nullable=False)
    amount: Mapped[float] = mapped_column(Float, nullable=False)

    budget: Mapped["Budget"] = relationship("Budget")
    goal: Mapped["Goal"] = relationship("Goal", back_populates="real_savings")

    supports_budget_filter = True # possible to filter by "budget_id"


