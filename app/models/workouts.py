from sqlalchemy import Column, Integer, DateTime, Text, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


class Workout(Base):
    __tablename__ = "workouts"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    date = Column(DateTime, nullable=False)
    notes = Column(Text)

    exercise_entries = relationship("ExerciseEntry", cascade="all, delete-orphan")
