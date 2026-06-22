from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.utils.auth import create_access_token, get_password_hash, verify_password, oauth2_scheme
from app.schemas.auth import RegisterRequest, LoginRequest, Token

auth_router = APIRouter()


@auth_router.post("/auth/register", response_model=Token)
def register(request: RegisterRequest, db: Session = Depends(get_db)):
    # Lazy import to avoid duplicate table registration
    from app.models.users import User

    existing_user = db.query(User).filter(User.email == request.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_pwd = get_password_hash(request.password)
    new_user = User(
        username=request.username,
        email=request.email,
        hashed_password=hashed_pwd,
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    access_token = create_access_token(data={"sub": str(new_user.id)})
    return Token(access_token=access_token, token_type="bearer")


@auth_router.post("/auth/login", response_model=Token)
def login(request: LoginRequest, db: Session = Depends(get_db)):
    from app.models.users import User

    user = db.query(User).filter(User.email == request.email).first()
    if not user or not verify_password(request.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    access_token = create_access_token(data={"sub": str(user.id)})
    return Token(access_token=access_token, token_type="bearer")
