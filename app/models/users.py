from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship

from app.database import Base


class User(Base):
    __tablename__ = "users"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    reminder_enabled = Column(Boolean, nullable=False)
    reminder_time = Column(String, nullable=True)

    # Relationships to other tables that reference users.id
    workouts = relationship("Workout" )
