from datetime import date
from typing import Optional

from pydantic import BaseModel, Field, ConfigDict

class WorkoutCreate(BaseModel):
    date: date
    notes: Optional[str] = None

class WorkoutUpdate(BaseModel):
    date: Optional[date] = None
    notes: Optional[str] = None

class WorkoutResponse(BaseModel):
    id: int
    date: date
    notes: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)

