from fastapi import FastAPI

# Database
from app.database import engine, Base

# Models (import all to register tables)
from app.models.exercise_entries import *  # noqa: F401
from app.models.users import *  # noqa: F401
from app.models.workouts import *  # noqa: F401
from app.models.sets import *  # noqa: F401
from app.models.personal_records import *  # noqa: F401

# Routers
from app.routes.user_routes import user_router
from app.routes.auth_routes import auth_router
from app.routes.set_item_routes import set_item_router
from app.routes.exercise_entry_routes import exercise_entry_router
from app.routes.personal_record_routes import personal_record_router
from app.routes.workout_routes import workout_router
from app.routes.stats_routes import stats_router

app = FastAPI()

# CORS (required for frontend access)
from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create tables
Base.metadata.create_all(bind=engine)

# Include routers
app.include_router(user_router)
app.include_router(auth_router)
app.include_router(set_item_router)
app.include_router(exercise_entry_router)
app.include_router(personal_record_router)
app.include_router(workout_router)
app.include_router(stats_router)

# Health endpoint (required for deployment health checks)
@app.get("/health")
def health():
    return {"status": "ok", "version": "1.0"}

# Serve React frontend (must be last — catches all remaining routes)
import os
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

_DIST = os.path.join(os.path.dirname(os.path.dirname(__file__)), "dist")

if os.path.exists(_DIST):
    app.mount("/assets", StaticFiles(directory=os.path.join(_DIST, "assets")), name="assets")

    @app.get("/{full_path:path}")
    async def serve_spa(full_path: str):
        return FileResponse(os.path.join(_DIST, "index.html"))
