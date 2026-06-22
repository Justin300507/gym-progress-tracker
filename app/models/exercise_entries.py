from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


class ExerciseEntry(Base):
    __tablename__ = "exercise_entries"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True, nullable=False)
    workout_id = Column(Integer, ForeignKey("workouts.id"), nullable=False)
    exercise_name = Column(String, nullable=False)

    workout = relationship("Workout", back_populates="exercise_entries")
    sets = relationship("Set", back_populates="exercise_entry", cascade="all, delete-orphan")
