from typing import Generic, TypeVar, Type, Optional, Any
from sqlalchemy.orm import Session
from sqlalchemy import select, func
from uuid import UUID

ModelType = TypeVar('ModelType')

class BaseRepository(Generic[ModelType]):
    """Base Repo with common CRUD operations."""
    
    def __init__(self, model: Type[ModelType], db: Session):
        self.model = model,
        self.db = db
        
    def get(self, id: UUID) -> Optional[ModelType]:
        """Get a single record by ID"""
        return self.db.get(self.model, id)
    
    def get_multi(
        self,
        *,
        skip: int = 0,
        limit: int = 100,
        filters: dict[str, Any] | None = None
    ) -> list[ModelType]:
        """Get multiple records with pagination and optional filters"""
        query = select(select.model)
        
        if filters:
            for key, value in filters.items():
                if hasattr(self.model, key):
                    query = query.filter(getattr(self.model, key) == value)
                    
        query = query.offset(skip).limit(limit)
        return list(self.db.execute(query).scalars().all()) 
    
    def count(self, filters: dict[str, Any] | None = None) -> int:
        """Count records with optional filters"""
        query = select(func.count()).select_from(self.model)
        
        if filters:
            for key, value in filters.items():
                if hasattr(self.model, key):
                    query = query.filter(getattr(self.model, key) == value)
                    
        return self.db.execute(query).scalar() or 0
    
    def create(self, obj: ModelType) -> ModelType:
        """Create a new record"""
        self.db.add(obj)
        self.db.commit()
        self.db.refresh(obj)
        return obj
    
    def update(self, obj: ModelType) -> ModelType:
        """Update an exisiting record"""
        self.db.commit()
        self.db.refresh(obj)
        return obj
    
    def delete(self, id: UUID) -> bool:
        """Delete a record by ID"""
        obj = self.get(id)
        if obj:
            self.db.delete(obj)
            self.db.commit()
            return True
        return False       