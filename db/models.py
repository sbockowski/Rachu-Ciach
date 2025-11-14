# db/models.py
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Text
from sqlalchemy.orm import relationship
from db.session import Base

class Budget(Base):
    __tablename__ = "budget"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    created_at = Column(String, nullable=False)      # TEXT 'YYYY-MM-DD HH:MM:SS'

    spend_plans = relationship("SpendPlan", back_populates="budget", cascade="all, delete-orphan")
    income_plans = relationship("IncomePlan", back_populates="budget", cascade="all, delete-orphan")
    real_spends = relationship("RealSpend", back_populates="budget", cascade="all, delete-orphan")

class Category(Base):
    __tablename__ = "category"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)

    spend_plans = relationship("SpendPlan", back_populates="category")
    real_spends = relationship("RealSpend", back_populates="category")

class IncomeType(Base):
    __tablename__ = "income_type"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)

    income_plans = relationship("IncomePlan", back_populates="type")
    real_incomes = relationship("RealIncome", back_populates="type")

class Goal(Base):
    __tablename__ = "goal"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)

    savings_plans = relationship("SavingsPlan", back_populates="goal")
    real_savings = relationship("RealSavings", back_populates="goal")

class IncomePlan(Base):
    __tablename__ = "income_plan"

    id = Column(Integer, primary_key=True)
    budget_id = Column(Integer, ForeignKey("budget.id"), nullable=False)
    type_id = Column(Integer, ForeignKey("income_type.id"), nullable=False)
    amount = Column(Float, nullable=False)

    budget = relationship("Budget", back_populates="income_plans")
    type = relationship("IncomeType", back_populates="income_plans")

class SpendPlan(Base):
    __tablename__ = "spend_plan"

    id = Column(Integer, primary_key=True)
    budget_id = Column(Integer, ForeignKey("budget.id"), nullable=False)
    category_id = Column(Integer, ForeignKey("category.id"), nullable=False)
    amount = Column(Float, nullable=False)

    budget = relationship("Budget", back_populates="spend_plans")
    category = relationship("Category", back_populates="spend_plans")

class SavingsPlan(Base):
    __tablename__ = "savings_plan"

    id = Column(Integer, primary_key=True)
    budget_id = Column(Integer, ForeignKey("budget.id"), nullable=False)
    goal_id = Column(Integer, ForeignKey("goal.id"), nullable=False)
    amount = Column(Float, nullable=False)

    budget = relationship("Budget")
    goal = relationship("Goal", back_populates="savings_plans")

class RealIncome(Base):
    __tablename__ = "real_income"

    id = Column(Integer, primary_key=True)
    budget_id = Column(Integer, ForeignKey("budget.id"), nullable=False)
    type_id = Column(Integer, ForeignKey("income_type.id"), nullable=False)
    amount = Column(Float, nullable=False)

    budget = relationship("Budget", back_populates="real_incomes")
    type = relationship("IncomeType", back_populates="real_incomes")

class RealSpend(Base):
    __tablename__ = "real_spend"

    id = Column(Integer, primary_key=True)
    budget_id = Column(Integer, ForeignKey("budget.id"), nullable=False)
    category_id = Column(Integer, ForeignKey("category.id"), nullable=False)
    amount = Column(Float, nullable=False)

    budget = relationship("Budget", back_populates="real_spends")
    category = relationship("Category", back_populates="real_spends")

class RealSavings(Base):
    __tablename__ = "real_savings"

    id = Column(Integer, primary_key=True)
    budget_id = Column(Integer, ForeignKey("budget.id"), nullable=False)
    goal_id = Column(Integer, ForeignKey("goal.id"), nullable=False)
    amount = Column(Float, nullable=False)

    budget = relationship("Budget")
    goal = relationship("Goal", back_populates="real_savings")
