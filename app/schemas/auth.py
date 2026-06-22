from typing import Optional

from pydantic import BaseModel, Field, ConfigDict


class RegisterRequest(BaseModel):
    username: str = Field(min_length=1)
    email: str = Field(min_length=1)
    password: str = Field(min_length=1)

    model_config = ConfigDict(from_attributes=True)


class LoginRequest(BaseModel):
    username: str = Field(min_length=1)
    password: str = Field(min_length=1)

    model_config = ConfigDict(from_attributes=True)


class Token(BaseModel):
    access_token: str = Field(min_length=1)
    token_type: str = Field(default="bearer", min_length=1)

    model_config = ConfigDict(from_attributes=True)


class AuthCreate(BaseModel):
    username: str = Field(min_length=1)
    email: str = Field(min_length=1)
    password: str = Field(min_length=1)

    model_config = ConfigDict(from_attributes=True)


class AuthUpdate(BaseModel):
    username: Optional[str] = Field(default=None, min_length=1)
    email: Optional[str] = Field(default=None, min_length=1)
    password: Optional[str] = Field(default=None, min_length=1)

    model_config = ConfigDict(from_attributes=True)


class AuthResponse(BaseModel):
    id: int
    username: str
    email: str

    model_config = ConfigDict(from_attributes=True)
