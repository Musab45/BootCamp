from uuid import UUID
from fastapi import Depends
from typing import Annotated
from requests import Session
from app.core.exceptions import AuthenticationError
from app.db.core import get_db
from app.db.repositories.user_repository import UserRepository
from app.schemas.auth import TokenData
from fastapi.security import OAuth2PasswordBearer
from app.core.security import decode_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")

async def get_current_user(
    token: Annotated[str, Depends(oauth2_scheme)],
    db: Annotated[Session, Depends(get_db)],
) -> TokenData:
    """Get current authenticated user from token"""
    payload = decode_token(token)
    user_id: str | None = payload.get("sub")
    email: str | None = payload.get("email")
    
    if not user_id or not email:
        raise AuthenticationError("Token missing user_id or email")
    
    user_repo = UserRepository(db)
    user = user_repo.get_by_email(email)
    
    if not user:
        raise AuthenticationError("User not found")
    
    return TokenData(user_id=UUID(user_id), email= email)

