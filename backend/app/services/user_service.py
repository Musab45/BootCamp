from uuid import UUID, uuid4
from app.models.user import User
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.schemas.user import UserRegister, UserUpdate
from app.core.exceptions import NotFoundError, ConflictError
from app.db.repositories.user_repository import UserRepository
from app.core.security import get_password_hash, verify_password

class UserService:
    """Service for user related operations."""
    
    def __init__(self, db: Session):
        self.repository = UserRepository
        self.db = db
        
    def get_user(self, user_id: UUID):
        """Get a user by ID"""
        user = self.repository.get(user_id)
        if not user:
            raise NotFoundError("User not found")  
        return user
    
    def get_user_by_email(self, email: str):
        """Get a user by email"""
        user = self.repository.get_by_email(email)
        if not user:
            raise NotFoundError("User not found for the provided email")
        return user
    
    def create_user(self, user_data: UserRegister) -> User:
        """Create a new user"""
        try:
            # check if email exists
            if self.repository.email_exists(user_data.email):
                raise ConflictError(f"{user_data.email} is already being used")
            
            user = User(
                id = uuid4(),
                email = user_data.email,
                first_name = user_data.first_name,
                last_name = user_data.last_name,
                hashed_password = get_password_hash(user_data.password)
            )
            
            created_user = self.repository.create(user)
            return created_user
        except IntegrityError as e:
            self.db.rollback()
            raise ConflictError("Email already in use")
        except Exception as e:
            self.db.rollback()
            raise
        
    def update_user(self, user_id: UUID, user_data: UserUpdate) -> User:
        """Update an existing user"""
        user = self.repository.get(user_id)
        
        if not user:
            raise NotFoundError("User not found for the provided email")
        
        for  key, value in user_data.model_dump(exclude_unset=True).items():
            setattr(user, key, value)