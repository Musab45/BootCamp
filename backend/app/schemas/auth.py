from pydantic import BaseModel, EmailStr, Field
from uuid import UUID

class Token(BaseModel):
    """Token response schema"""
    
    access_token: str
    refresh_token: str
    token_type: str = "Bearer"
    
class TokenData(BaseModel):
    """Token payload data schema"""
    
    user_id: UUID
    email: str
    
class LoginRequest(BaseModel):
    """Login request schema"""
    
    email: EmailStr
    password: str = Field(..., min_length=1)