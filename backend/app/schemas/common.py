from pydantic import BaseModel

class Message(BaseModel):
    """Generic message reponse schema"""
    message: str