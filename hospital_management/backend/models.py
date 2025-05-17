"""
    Source Code for Database Tables
    How Data is stored in Database
"""

from sqlalchemy import (
    Column,
    Integer,
    String
)
from hospital_management.backend.database import Base

class User(Base):
    """
        users table
    """
    __tablename__ = "users"
    id = Column(Integer,primary_key=True,index=True)
    username = Column(String,unique=True,index=True , nullable=False)
    hashed_password = Column(String , nullable=False)
    fullname = Column(String,nullable=False)
    role = Column(String , nullable=False)
