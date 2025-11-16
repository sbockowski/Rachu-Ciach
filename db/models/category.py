from __future__ import annotations
from typing import List
from sqlalchemy import Integer, String
from sqlalchemy.orm import relationship, mapped_column, Mapped
from .base import Base

class Category(Base):
    __tablename__ = "category"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False, unique=True)

    spend_plans: Mapped[List["SpendPlan"]] = relationship("SpendPlan", back_populates="category")
    real_spends: Mapped[List["RealSpend"]] = relationship("RealSpend", back_populates="category")