from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.db.core import get_db
from app.schemas.user import UserResponse, UserUpdate, PasswordChange
from app.dependencies import CurrentUser
from app.services.user_service import UserService
from app.schemas.common import Message

router = APIRouter(prefix="/users", tags=["Users"])

@router.get(
    "/me",
    response_model=UserResponse,
    summary="Get current user",
    description="Get the proile of the currently authenticated user",
)
async def get_current_user(
    current_user: CurrentUser,
    db: Session = Depends(get_db)
):
    """Get current user profile"""
    user_service = UserService(db)
    return user_service.get_user(current_user.user_id)

@router.put(
    "/me",
    response_model=UserResponse,
    summary="Update Current User",
    description="Update the profile of the currently authenticated user",
)
async def update_current_user(
    user_update: UserUpdate,
    current_user: CurrentUser,
    db: Session = Depends(get_db),
):
    """Update current user profile"""
    user_service = UserService(db)
    return user_service.update_user(current_user.user_id, user_update)


@router.post(
    "/me/change-password",
    response_model=Message,
    status_code=status.HTTP_200_OK,
    summary="Change user password",
    description="Change password of the currently authenticated user",
)
async def change_password(
    password_change: PasswordChange,
    current_user: CurrentUser,
    db: Session = Depends(get_db),
):
    user_service = UserService(db)
    user_service.change_password(current_user.user_id, password_change)
    return Message(message="Password changed successfully")