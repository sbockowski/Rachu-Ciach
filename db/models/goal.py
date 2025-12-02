from __future__ import annotations
from typing import List
from sqlalchemy import Integer, String
from sqlalchemy.orm import relationship, mapped_column, Mapped
from .base import Base

class Goal(Base):
    __tablename__ = "goal"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False, unique=True)

    savings_plans: Mapped[List["SavingsPlan"]] = relationship("SavingsPlan", back_populates="goal")
    real_savings: Mapped[List["RealSavings"]] = relationship("RealSavings", back_populates="goal")

