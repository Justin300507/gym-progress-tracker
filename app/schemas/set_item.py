from pydantic import BaseModel, Field, ConfigDict
from typing import Optional


class SetItemCreate(BaseModel):
    set_number: int = Field(...)
    reps: int = Field(...)
    weight: float = Field(...)


class SetItemUpdate(BaseModel):
    set_number: Optional[int] = None
    reps: Optional[int] = None
    weight: Optional[float] = None


class SetItemResponse(BaseModel):
    id: int
    set_number: int
    reps: int
    weight: float

    model_config = ConfigDict(from_attributes=True)


class SetItemRead(BaseModel):
    id: int
    set_number: int
    reps: int
    weight: float

    model_config = ConfigDict(from_attributes=True)
