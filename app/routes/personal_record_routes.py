from fastapi import APIRouter, Depends, HTTPException, Path, Query
from sqlalchemy.orm import Session
from typing import List
from datetime import datetime

from app.database import get_db
from app.models.personal_records import PersonalRecords
from app.utils.auth import get_current_user, oauth2_scheme

# Import Pydantic schemas defined elsewhere to avoid duplicate definitions
from app.schemas.personal_record import PersonalRecordUpdate, PersonalRecordResponse

personal_record_router = APIRouter()

@personal_record_router.get("/personal_records", response_model=List[PersonalRecordResponse])
def list_personal_records(
    limit: int = Query(50, ge=1, le=500),
    offset: int = Query(0, ge=0),
    db: Session = Depends(get_db),
    current_user: "User" = Depends(get_current_user),
):
    records = (
        db.query(PersonalRecords)
        .filter(PersonalRecords.user_id == current_user.id)
        .offset(offset)
        .limit(limit)
        .all()
    )
    return records

@personal_record_router.patch("/personal_records/{id}", response_model=PersonalRecordResponse)
def update_personal_record(
    personal_record_in: PersonalRecordUpdate,
    id: int = Path(..., gt=0),
    db: Session = Depends(get_db),
    current_user: "User" = Depends(get_current_user),
):
    record = (
        db.query(PersonalRecords)
        .filter(PersonalRecords.id == id, PersonalRecords.user_id == current_user.id)
        .first()
    )
    if not record:
        raise HTTPException(status_code=404, detail="Not found")

    if personal_record_in.max_weight is not None:
        record.max_weight = personal_record_in.max_weight
    if personal_record_in.max_reps is not None:
        record.max_reps = personal_record_in.max_reps
    if personal_record_in.record_date is not None:
        record.record_date = personal_record_in.record_date

    db.add(record)
    db.commit()
    db.refresh(record)
    return record