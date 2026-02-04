from fastapi import APIRouter
from app.api.v1 import users, auth

api_router = APIRouter()

# sub-routers
api_router.include_router(auth.router)