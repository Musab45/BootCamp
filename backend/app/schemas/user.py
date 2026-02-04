from uuid import UUID
from datetime import datetime
from pydantic import BaseModel, ConfigDict, EmailStr, Field

class UserBase(BaseModel):
    """Base user schema"""
    email: EmailStr
    first_name: str = Field(..., min_length=1, max_length=255)
    last_name: str = Field(..., min_length=1, max_length=255)

class UserRegister(UserBase):
    """Schema for user registration"""
    password: str = Field(..., min_length=1, max_length=100, description='User password')
    
class UserUpdate(BaseModel):
    """Schema to update user info."""
    first_name: str | None = Field(..., min_length=1, max_length=255)
    last_name: str | None = Field(..., min_length=1, max_length=255)


class UserResponse(UserBase):
    """Schema for user response"""
    id: UUID
    created_at: datetime
    updated_at: datetime
    
    model_config = ConfigDict(from_attributes=True)
    
class PasswordChange(BaseModel):
    """Schema to change user password"""
    current_password: str = Field(..., min_length=1, max_length=100)
    new_password: str = Field(..., min_length=1, max_length=100)
    new_password_confirm: str = Field(..., min_length=1, max_length=100)