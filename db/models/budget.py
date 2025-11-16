from __future__ import annotations
from typing import List
from sqlalchemy import Integer, String
from sqlalchemy.orm import relationship, mapped_column, Mapped

class Budget(Base):
    __tablename__ = "budget"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    created_at: Mapped[str] = mapped_column(String, nullable=False)

    spend_plans: Mapped[List["SpendPlan"]] = relationship(
        "SpendPlan", back_populates="budget", cascade="all, delete-orphan"
    )
    income_plans: Mapped[List["IncomePlan"]] = relationship(
        "IncomePlan", back_populates="budget", cascade="all, delete-orphan"
    )
    real_spends: Mapped[List["RealSpend"]] = relationship(
        "RealSpend", back_populates="budget", cascade="all, delete-orphan"
    )