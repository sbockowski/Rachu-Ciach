from __future__ import annotations
from typing import List
from sqlalchemy import Integer, String
from sqlalchemy.orm import relationship, mapped_column, Mapped
from .base import Base

class Kind(Base):
    __tablename__ = "kind"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False, unique=True)

    income_plans: Mapped[List["IncomePlan"]] = relationship("IncomePlan", back_populates="kind", cascade="all, delete-orphan")
    real_incomes: Mapped[List["RealIncome"]] = relationship("RealIncome", back_populates="kind", cascade="all, delete-orphan")

    supports_budget_filter = False # possible to filter by "id", but not "budget_id"