from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from app.database import Base


class User(Base):
    __tablename__ = "users"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True, nullable=False)
    username = Column(String, nullable=False, default="")
    email = Column(String, nullable=False, unique=True)
    hashed_password = Column(String, nullable=False)
    reminder_enabled = Column(Boolean, nullable=False, default=False)
    reminder_time = Column(String, nullable=True)
