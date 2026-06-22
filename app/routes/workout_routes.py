from fastapi import APIRouter, Depends, HTTPException, Query, Path
from sqlalchemy.orm import Session, joinedload
from pydantic import BaseModel, Field, ConfigDict

from app.database import get_db
from app.models.workout import Workout
from app.models.exercise_entries import ExerciseEntry
from app.schemas.workout import WorkoutCreate, WorkoutUpdate, WorkoutResponse
from app.utils.auth import get_current_user, oauth2_scheme
from app.schemas.auth import RegisterRequest, LoginRequest, Token

# ---------------------------------------------------------------------------
# Router definition
# ---------------------------------------------------------------------------

workout_router = APIRouter()

# ---------------------------------------------------------------------------
# Endpoints
# ---------------------------------------------------------------------------

@workout_router.get("/workouts", response_model=list[WorkoutResponse])
def list_workouts(
    limit: int = Query(50, ge=1, le=500),
    offset: int = Query(0, ge=0),
    db: Session = Depends(get_db),
    current_user: "User" = Depends(get_current_user),
):
    """List workouts belonging to the authenticated user with pagination."""
    workouts = (
        db.query(Workout)
        .filter(Workout.user_id == current_user.id)
        .offset(offset)
        .limit(limit)
        .all()
    )
    return workouts

@workout_router.post("/workouts", response_model=WorkoutResponse, status_code=201)
def create_workout(
    workout_in: WorkoutCreate,
    db: Session = Depends(get_db),
    current_user: "User" = Depends(get_current_user),
):
    """Create a new workout for the authenticated user."""
    workout = Workout(
        user_id=current_user.id,
        date=workout_in.date,
        notes=workout_in.notes,
    )
    db.add(workout)
    db.commit()
    db.refresh(workout)
    return workout

@workout_router.get("/workouts/{workout_id}", response_model=WorkoutResponse)
def get_workout(
    workout_id: int = Path(...),
    db: Session = Depends(get_db),
    current_user: "User" = Depends(get_current_user),
):
    """Retrieve a specific workout with its exercises and sets."""
    workout = (
        db.query(Workout)
        .options(
            joinedload(Workout.exercise_entries).joinedload(ExerciseEntry.sets)
        )
        .filter(Workout.id == workout_id, Workout.user_id == current_user.id)
        .first()
    )
    if not workout:
        raise HTTPException(status_code=404, detail="Not found")
    return workout

@workout_router.put("/workouts/{workout_id}", response_model=WorkoutResponse)
def update_workout(
    workout_in: WorkoutUpdate,
    workout_id: int = Path(...),
    db: Session = Depends(get_db),
    current_user: "User" = Depends(get_current_user),
):
    """Update workout details for the owner."""
    workout = (
        db.query(Workout)
        .filter(Workout.id == workout_id, Workout.user_id == current_user.id)
        .first()
    )
    if not workout:
        raise HTTPException(status_code=404, detail="Not found")
    if workout_in.date is not None:
        workout.date = workout_in.date
    if workout_in.notes is not None:
        workout.notes = workout_in.notes
    db.commit()
    db.refresh(workout)
    return workout

@workout_router.delete("/workouts/{workout_id}", status_code=204)
def delete_workout(
    workout_id: int = Path(...),
    db: Session = Depends(get_db),
    current_user: "User" = Depends(get_current_user),
):
    """Delete a workout and all related exercise entries and sets."""
    workout = (
        db.query(Workout)
        .filter(Workout.id == workout_id, Workout.user_id == current_user.id)
        .first()
    )
    if not workout:
        raise HTTPException(status_code=404, detail="Not found")
    db.delete(workout)
    db.commit()
    return
