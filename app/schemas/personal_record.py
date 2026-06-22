from datetime import date
from typing import Optional

from pydantic import BaseModel, Field, ConfigDict

class PersonalRecordCreate(BaseModel):
    max_weight: float = Field(..., gt=0)
    max_reps: int = Field(..., gt=0)
    record_date: date = Field(...)

    model_config = ConfigDict(from_attributes=True)

class PersonalRecordUpdate(BaseModel):
    max_weight: Optional[float] = Field(None, gt=0)
    max_reps: Optional[int] = Field(None, gt=0)
    record_date: Optional[date] = None

    model_config = ConfigDict(from_attributes=True)

class PersonalRecordResponse(BaseModel):
    id: int
    max_weight: float
    max_reps: int
    record_date: date

    model_config = ConfigDict(from_attributes=True)

