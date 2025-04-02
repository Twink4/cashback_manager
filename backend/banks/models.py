from sqlalchemy import (
    Column,
    Integer,
    String
)

from backend.core.database import Base

class Banks(Base):
    __tablename__ = "banks"
    
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)