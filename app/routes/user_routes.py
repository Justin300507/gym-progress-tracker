from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from typing import Optional
from pydantic import BaseModel, Field, ConfigDict

from app.database import get_db
from app.utils.auth import get_current_user, oauth2_scheme

user_router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")

class UserPreferencesUpdate(BaseModel):
    reminder_enabled: Optional[bool] = None
    reminder_time: Optional[str] = Field(default=None, min_length=1)

    model_config = ConfigDict(from_attributes=True)

@user_router.get("/users/me")
def read_current_user(
    db: Session = Depends(get_db),
    current_user: "User" = Depends(get_current_user),
):
    """Return the authenticated user's profile."""
    return {
        "id": current_user.id,
        "email": current_user.email,
        "username": getattr(current_user, "username", None),
        "full_name": getattr(current_user, "full_name", None),
    }

@user_router.patch("/users/me")
def update_current_user(
    prefs: UserPreferencesUpdate,
    db: Session = Depends(get_db),
    current_user: "User" = Depends(get_current_user),
):
    """Update user preferences such as reminder settings."""
    updated = False
    if prefs.reminder_enabled is not None:
        setattr(current_user, "reminder_enabled", prefs.reminder_enabled)
        updated = True
    if prefs.reminder_time is not None:
        setattr(current_user, "reminder_time", prefs.reminder_time)
        updated = True
    if not updated:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No fields to update",
        )
    db.add(current_user)
    db.commit()
    db.refresh(current_user)
    return {
        "id": current_user.id,
        "email": current_user.email,
        "username": getattr(current_user, "username", None),
        "full_name": getattr(current_user, "full_name", None),
        "reminder_enabled": getattr(current_user, "reminder_enabled", None),
        "reminder_time": getattr(current_user, "reminder_time", None),
    }
