from sqlalchemy import Column, Integer, String
from database import Base

class Branch(Base):
    __tablename__ = "branches"

    id = Column(Integer, primary_key=True, index=True)
    branch_name = Column(String, index=True)
    ip = Column(String, unique=True, index=True)
