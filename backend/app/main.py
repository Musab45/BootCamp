from fastapi import FastAPI
from app.api.v1.router import api_router
from app.config import get_settings
from app.core.exceptions import BootCampExceptions, bootcamp_exception_handler

settings = get_settings()

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="BootCamp",
)

app.add_exception_handler(BootCampExceptions, bootcamp_exception_handler)

app.include_router(api_router, prefix="/api/v1")

@app.get("/", tags=["Root"])
async def root():
    """Root endpoint with API information"""
    return{
        "message": "Welcome to BootCamp",
        "version": settings.app_version,
        "docs": "/api/docs",
    }