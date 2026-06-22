from fastapi import APIRouter, Depends, HTTPException, Path
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.workout import Workout
from app.models.exercise_entries import ExerciseEntry
from app.schemas.exercise_entry import ExerciseEntryCreate, ExerciseEntryResponse
from app.utils.auth import get_current_user

exercise_entry_router = APIRouter()

@exercise_entry_router.post("/workouts/{workout_id}/exercises", response_model=ExerciseEntryResponse)
def add_exercise_entry(
    entry_in: ExerciseEntryCreate,
    workout_id: int = Path(..., ge=1),
    db: Session = Depends(get_db),
    current_user: "User" = Depends(get_current_user),
):
    # Verify workout exists and belongs to the current user
    workout = db.query(Workout).filter(Workout.id == workout_id).first()
    if not workout:
        raise HTTPException(status_code=404, detail="Workout not found")
    if workout.user_id != current_user.id:
        raise HTTPException(status_code=404, detail="Workout not found")
    # Create exercise entry
    exercise_entry = ExerciseEntry(name=entry_in.name, workout_id=workout.id)
    db.add(exercise_entry)
    db.commit()
    db.refresh(exercise_entry)
    return ExerciseEntryResponse.from_orm(exercise_entry)
