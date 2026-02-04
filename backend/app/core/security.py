from backend.app.config import get_settings
from passlib.context import CryptContext

settings = get_settings()

# password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str) -> str:
    """Generate a password hash"""
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify a plain password against a password hash"""
    return pwd_context.verify(plain_password, hashed_password)

