from datetime import datetime
from sqlalchemy import DateTime, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    """Base Class for DB Models"""
    pass

class TimeStampMixin:
    """Mixin to add create and update timestamps"""
    
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )
    
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False
    )
    
class SoftDeleteMixin:
    """Mixin to add soft delete functionality"""
    
    deleted_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
        default=None
    )
    
    def soft_delete(self) -> None:
        """Mark this record as deleted"""
        self.deleted_at = func.now()
        
    @property
    def is_deleted(self) -> bool:
        """Check if record is deleted"""
        return self.deleted_at is not None