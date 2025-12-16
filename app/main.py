from fastapi import FastAPI
from app.api.router import api_router
from app.core.config import settings
from app.core.logger import setup_logging

# Set up logging
setup_logging()

# Create FastAPI app
app = FastAPI(
    title="My FastAPI Backend",
    description="A complete FastAPI backend with clean architecture.",
    version="0.1.0",
)

# Include the API router
app.include_router(api_router, prefix="/api/v1")

@app.get("/")
def read_root():
    """
    Root endpoint.
    """
    return {"message": "Welcome to the FastAPI application!"}

