from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey
)

from backend.core.database import Base


class MccCodes(Base):
    __tablename__ = "mcc_codes"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    mcc_code = Column(String, nullable=False, unique=True)
    base_cashback_category_id = Column(
        ForeignKey("cashback_category.id"), nullable=False)
