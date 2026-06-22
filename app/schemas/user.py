from typing import Optional

from pydantic import BaseModel, Field, ConfigDict

class UserCreate(BaseModel):
    username: str = Field(min_length=1)
    email: str = Field(min_length=1)
    full_name: str = Field(min_length=1)
    password: str = Field(min_length=1)

    model_config = ConfigDict(from_attributes=True)

class UserUpdate(BaseModel):
    full_name: Optional[str] = None
    email: Optional[str] = None
    reminder_enabled: Optional[bool] = None
    reminder_time: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)

class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    full_name: Optional[str] = None
    reminder_enabled: Optional[bool] = None
    reminder_time: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)

