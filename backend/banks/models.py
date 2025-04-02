from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey
)

from backend.core.database import Base


class Banks(Base):
    __tablename__ = "banks"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String, nullable=False, unique=True)


class CashbackCategory(Base):
    __tablename__ = "cashback_category"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String, nullable=False, unique=True)


class CashbackCategoryWithBank(Base):
    __tablename__ = "cashback_category_with_bank"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    bank_id = Column(ForeignKey("banks.id"), nullable=False)
    mcc_code = Column(Integer, nullable=False)
    cashback_category_id = Column(ForeignKey(
        "cashback_category.id"), nullable=False)
