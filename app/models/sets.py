from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Set(Base):
    __tablename__ = "sets"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True, nullable=False)
    exercise_entry_id = Column(Integer, ForeignKey('exercise_entries.id'), nullable=False)
    set_number = Column(Integer, nullable=False)
    reps = Column(Integer, nullable=False)
    weight = Column(Float, nullable=False)

    exercise_entry = relationship("ExerciseEntry", back_populates="sets")
