from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from sqlalchemy import func
from datetime import datetime, timedelta

from app.database import get_db
from app.models.set import Set
from app.models.exercise_entries import ExerciseEntry
from app.models.workout import Workout
from app.models.user import User
from app.utils.auth import get_current_user

stats_router = APIRouter()

@stats_router.get("/stats/weekly_volume")
def weekly_volume(
    limit: int = Query(50, ge=1, le=500),
    offset: int = Query(0, ge=0),
    db: Session = Depends(get_db),
):
    """Return total volume per week for the past 8 weeks.
    Volume is calculated as sum of weight * reps for all sets in a week.
    """
    start_date = datetime.utcnow() - timedelta(weeks=8)
    # Join Set -> ExerciseEntry -> Workout to access the workout date and filter by date range
    results = (
        db.query(
            func.date_trunc('week', Workout.date).label('week_start'),
            func.sum(Set.weight * Set.reps).label('total_volume'),
        )
        .join(ExerciseEntry, Set.exercise_entry_id == ExerciseEntry.id)
        .join(Workout, ExerciseEntry.workout_id == Workout.id)
        .filter(Workout.date >= start_date)
        .group_by('week_start')
        .order_by('week_start')
        .offset(offset)
        .limit(limit)
        .all()
    )
    return [
        {"week_start": week_start.date().isoformat(), "total_volume": float(total_volume or 0)}
        for week_start, total_volume in results
    ]

@stats_router.get("/stats/exercise_aggregates")
def exercise_aggregates(
    limit: int = Query(50, ge=1, le=500),
    offset: int = Query(0, ge=0),
    db: Session = Depends(get_db),
    current_user: "User" = Depends(get_current_user),
):
    """Return max weight, max reps, and total volume per exercise for the authenticated user.
    Volume is calculated as sum of weight * reps for each exercise.
    """
    results = (
        db.query(
            ExerciseEntry.name.label('exercise_name'),
            func.max(Set.weight).label('max_weight'),
            func.max(Set.reps).label('max_reps'),
            func.sum(Set.weight * Set.reps).label('total_volume'),
        )
        .join(Set, Set.exercise_entry_id == ExerciseEntry.id)
        .join(Workout, ExerciseEntry.workout_id == Workout.id)
        .filter(Workout.user_id == current_user.id)
        .group_by(ExerciseEntry.name)
        .order_by(ExerciseEntry.name)
        .offset(offset)
        .limit(limit)
        .all()
    )
    return [
        {
            "exercise_name": exercise_name,
            "max_weight": float(max_weight) if max_weight is not None else None,
            "max_reps": int(max_reps) if max_reps is not None else None,
            "total_volume": float(total_volume or 0),
        }
        for exercise_name, max_weight, max_reps, total_volume in results
    ]
