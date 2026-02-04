from typing import Optional
from requests import Session
from sqlalchemy import select, exists
from app.models.user import User
from app.db.repositories.base import BaseRepository

class UserRepository(BaseRepository[User]):
    """Repository for User model operations"""
    
    def __init__(self, db: Session):
        super().__init__(User, db)
        
    def get_by_email(self, email: str) -> Optional[User]:
        """Get User by email"""
        query = select(User).filter(User.email == email)
        return self.db.execute(query).scalar_one_or_none()
    
    def email_exists(self, email: str) -> bool:
        """Check if an email exists"""
        query = select(exists().where(User.email == email))
        return self.db.execute(query).scalar()