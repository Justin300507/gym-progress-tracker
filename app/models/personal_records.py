from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from app.database import Base


class PersonalRecords(Base):
    __tablename__ = "personal_records"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    exercise_name = Column(String, nullable=False)
    max_weight = Column(Float, nullable=False)
    max_reps = Column(Integer, nullable=False)
    record_date = Column(DateTime, nullable=False)


Personal_records = PersonalRecords
