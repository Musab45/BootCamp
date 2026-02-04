from uuid import UUID, uuid4
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import Mapped, mapped_column
from backend.app.db.base import Base, TimeStampMixin

class User(Base, TimeStampMixin):
    """User Model"""
    
    __tablename__ = "users"
    
    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    first_name: Mapped[str] = mapped_column(String(255), nullable=False)
    last_name: Mapped[str] = mapped_column(String(255), nullable=False)
    email: Mapped[str] = mapped_column(String(255),index=True, unique=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String(255), nullable=False)
    
    def __repr__(self) -> str:
        return f"<User(email='{self.email}', first_name='{self.first_name}', last_email='{self.last_name}')>"