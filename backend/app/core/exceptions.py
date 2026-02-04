from datetime import datetime
from fastapi import HTTPException, Request

class BootCampExceptions(Exception):
    """Base exceptions for BootCamp errors"""
    
    def __init__(self, message: str, status_code: int = 500):
        self.message = message
        self.status_code = status_code
        super.__init__(self.message)
        
class NotFoundError(BootCampExceptions):
    """Exceptions raised when a resource is not found"""
    
    def __init__(self, message = "Resource not found"):
        super().__init__(message, status_code = 404)
        
class ConflictError(BootCampExceptions):
    """Exceptions raised when a resource conflict occurs"""
    
    def __init__(self, message = "Resource conflict"):
        super().__init__(message, 404)