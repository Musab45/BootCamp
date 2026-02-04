from app.schemas.common import Message
from app.schemas.user import UserRegister
from app.schemas.auth import Token, LoginRequest
from app.services.user_service import UserService
from app.services.auth_service import AuthService
from app.db.core import get_db
from fastapi import APIRouter, status, Request, Depends
from sqlalchemy.orm import Session

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post(
    "/register",
    response_model=Message,
    status_code=status.HTTP_201_CREATED,
    summary="Register a new user",
    description="Create a new user account with email and password",
)
async def register(
    request: Request,
    user_data: UserRegister,
    db: Session = Depends(get_db)
):
    """Register a new user"""
    user_service = UserService(db)
    user_service.create_user(user_data)
    return Message(message="User registered Successfully")

@router.post(
    "/login",
    response_model=Token,
    summary="Login to get access token",
    description="Authenticate with email and password to get JWT tokens",
)
async def login(
    login_data: LoginRequest,
    db: Session = Depends(get_db)
):
    """Login adn receive access and refresh token"""
    auth_service = AuthService(db)
    return auth_service.authenticate_user(login_data.email, login_data.password)