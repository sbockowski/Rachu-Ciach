# db/models.py
from __future__ import annotations
from typing import List
from sqlalchemy import Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship, mapped_column, Mapped, DeclarativeBase

class Base(DeclarativeBase):
    pass
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

class Category(Base):
    __tablename__ = "category"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False, unique=True)

    spend_plans: Mapped[List["SpendPlan"]] = relationship("SpendPlan", back_populates="category")
    real_spends: Mapped[List["RealSpend"]] = relationship("RealSpend", back_populates="category")


class IncomeType(Base):
    __tablename__ = "income_type"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False, unique=True)

    income_plans: Mapped[List["IncomePlan"]] = relationship("IncomePlan", back_populates="type")
    real_incomes: Mapped[List["RealIncome"]] = relationship("RealIncome", back_populates="type")


class Goal(Base):
    __tablename__ = "goal"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False, unique=True)

    savings_plans: Mapped[List["SavingsPlan"]] = relationship("SavingsPlan", back_populates="goal")
    real_savings: Mapped[List["RealSavings"]] = relationship("RealSavings", back_populates="goal")


class IncomePlan(Base):
    __tablename__ = "income_plan"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    budget_id: Mapped[int] = mapped_column(ForeignKey("budget.id"), nullable=False)
    type_id: Mapped[int] = mapped_column(ForeignKey("income_type.id"), nullable=False)
    amount: Mapped[float] = mapped_column(Float, nullable=False)

    budget: Mapped["Budget"] = relationship("Budget", back_populates="income_plans")
    type: Mapped["IncomeType"] = relationship("IncomeType", back_populates="income_plans")


class SpendPlan(Base):
    __tablename__ = "spend_plan"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    budget_id: Mapped[int] = mapped_column(ForeignKey("budget.id"), nullable=False)
    category_id: Mapped[int] = mapped_column(ForeignKey("category.id"), nullable=False)
    amount: Mapped[float] = mapped_column(Float, nullable=False)

    budget: Mapped["Budget"] = relationship("Budget", back_populates="spend_plans")
    category: Mapped["Category"] = relationship("Category", back_populates="spend_plans")


class SavingsPlan(Base):
    __tablename__ = "savings_plan"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    budget_id: Mapped[int] = mapped_column(ForeignKey("budget.id"), nullable=False)
    goal_id: Mapped[int] = mapped_column(ForeignKey("goal.id"), nullable=False)
    amount: Mapped[float] = mapped_column(Float, nullable=False)

    budget: Mapped["Budget"] = relationship("Budget")
    goal: Mapped["Goal"] = relationship("Goal", back_populates="savings_plans")


class RealIncome(Base):
    __tablename__ = "real_income"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    budget_id: Mapped[int] = mapped_column(ForeignKey("budget.id"), nullable=False)
    type_id: Mapped[int] = mapped_column(ForeignKey("income_type.id"), nullable=False)
    amount: Mapped[float] = mapped_column(Float, nullable=False)

    budget: Mapped["Budget"] = relationship("Budget", back_populates="real_incomes")
    type: Mapped["IncomeType"] = relationship("IncomeType", back_populates="real_incomes")


class RealSpend(Base):
    __tablename__ = "real_spend"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    budget_id: Mapped[int] = mapped_column(ForeignKey("budget.id"), nullable=False)
    category_id: Mapped[int] = mapped_column(ForeignKey("category.id"), nullable=False)
    amount: Mapped[float] = mapped_column(Float, nullable=False)

    budget: Mapped["Budget"] = relationship("Budget", back_populates="real_spends")
    category: Mapped["Category"] = relationship("Category", back_populates="real_spends")


class RealSavings(Base):
    __tablename__ = "real_savings"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    budget_id: Mapped[int] = mapped_column(ForeignKey("budget.id"), nullable=False)
    goal_id: Mapped[int] = mapped_column(ForeignKey("goal.id"), nullable=False)
    amount: Mapped[float] = mapped_column(Float, nullable=False)

    budget: Mapped["Budget"] = relationship("Budget")
    goal: Mapped["Goal"] = relationship("Goal", back_populates="real_savings")
