from datetime import datetime, timezone
from fastapi import HTTPException, Request
from fastapi.responses import JSONResponse

class BootCampExceptions(Exception):
    """Base exceptions for BootCamp errors"""
    
    def __init__(self, message: str, status_code: int = 500):
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)
        
class NotFoundError(BootCampExceptions):
    """Exceptions raised when a resource is not found"""
    
    def __init__(self, message = "Resource not found"):
        super().__init__(message, status_code = 404)
        
class ConflictError(BootCampExceptions):
    """Exceptions raised when a resource conflict occurs"""
    
    def __init__(self, message = "Resource conflict"):
        super().__init__(message, 404)
        
class AuthenticationError(BootCampExceptions):
    """Exception raised for autherization errors"""
    
    def __init__(self, message: str = "Could not validate credentials"):
        super().__init__(message, status_code=401)
        
class ValidationError(BootCampExceptions):
    """Exception raised for validation errors."""
    
    def __init__(self, message: str = "Validation error"):
        super().__init__(message, status_code=400)
        
async def bootcamp_exception_handler(request: Request, exc: BootCampExceptions) -> JSONResponse:
    """Global Exception handler for BootCamp"""
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "detail": exc.message,
            "path": str(request.url),
            "timestamp": datetime.now(timezone.utc).isoformat()
        },
    )