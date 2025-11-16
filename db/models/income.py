from __future__ import annotations
from typing import List
from sqlalchemy import Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship, mapped_column, Mapped
from .base import Base

class IncomePlan(Base):
    __tablename__ = "income_plan"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    budget_id: Mapped[int] = mapped_column(ForeignKey("budget.id"), nullable=False)
    type_id: Mapped[int] = mapped_column(ForeignKey("income_type.id"), nullable=False)
    amount: Mapped[float] = mapped_column(Float, nullable=False)

    budget: Mapped["Budget"] = relationship("Budget", back_populates="income_plans")
    type: Mapped["IncomeType"] = relationship("IncomeType", back_populates="income_plans")

class RealIncome(Base):
    __tablename__ = "real_income"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    budget_id: Mapped[int] = mapped_column(ForeignKey("budget.id"), nullable=False)
    type_id: Mapped[int] = mapped_column(ForeignKey("income_type.id"), nullable=False)
    amount: Mapped[float] = mapped_column(Float, nullable=False)

    budget: Mapped["Budget"] = relationship("Budget", back_populates="real_incomes")
    type: Mapped["IncomeType"] = relationship("IncomeType", back_populates="real_incomes")
