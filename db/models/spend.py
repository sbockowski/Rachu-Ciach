from __future__ import annotations
from typing import List
from .base import Base
from sqlalchemy import Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship, mapped_column, Mapped

class SpendPlan(Base):
    __tablename__ = "spend_plan"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    budget_id: Mapped[int] = mapped_column(ForeignKey("budget.id"), nullable=False)
    category_id: Mapped[int] = mapped_column(ForeignKey("category.id"), nullable=False)
    amount: Mapped[float] = mapped_column(Float, nullable=False)

    budget: Mapped["Budget"] = relationship("Budget", back_populates="spend_plans")
    category: Mapped["Category"] = relationship("Category", back_populates="spend_plans")

class RealSpend(Base):
    __tablename__ = "real_spend"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    budget_id: Mapped[int] = mapped_column(ForeignKey("budget.id"), nullable=False)
    category_id: Mapped[int] = mapped_column(ForeignKey("category.id"), nullable=False)
    amount: Mapped[float] = mapped_column(Float, nullable=False)

    budget: Mapped["Budget"] = relationship("Budget", back_populates="real_spends")
    category: Mapped["Category"] = relationship("Category", back_populates="real_spends")