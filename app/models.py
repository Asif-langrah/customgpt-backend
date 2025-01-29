# app/models.py

from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    hashed_password = Column(String(128), nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    contact_number = Column(String(20), nullable=True)
    program = Column(String(100), nullable=True)
    is_enrolled = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
