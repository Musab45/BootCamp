from requests import Session
from app.schemas.auth import Token
from app.core.security import create_refresh_token, verify_password, create_access_token
from app.core.exceptions import AuthenticationError
from app.db.repositories.user_repository import UserRepository


class AuthService:
    """Service for authentication operations"""
    
    def __init__(self, db: Session):
        self.user_repository = UserRepository(db)
        
    def authenticate_user(self, email: str, password: str) -> Token:
        """Authenticate user and return token"""
        
        user = self.user_repository.get_by_email(email)
        
        if not user:
            raise AuthenticationError("Incorrect email or password")
        
        if not verify_password(password, user.hashed_password):
            raise AuthenticationError("Incorrect email or password")
        
        # create token
        token_data = {"sub": str(user.id), "email": str(user.email)}
        access_token = create_access_token(token_data)
        refresh_token = create_refresh_token(token_data)
        
        return Token(
            access_token=access_token,
            refresh_token=refresh_token,
            token_type="Bearer"
        )
        