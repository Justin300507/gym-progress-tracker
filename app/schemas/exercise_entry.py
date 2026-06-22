from typing import Optional
from pydantic import BaseModel, Field, ConfigDict

class ExerciseEntryCreate(BaseModel):
    name: str = Field(min_length=1)

class ExerciseEntryUpdate(BaseModel):
    name: Optional[str] = None

class ExerciseEntryResponse(BaseModel):
    id: int
    name: str

    model_config = ConfigDict(from_attributes=True)
