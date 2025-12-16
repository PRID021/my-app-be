from fastapi import APIRouter
from app.api.v1 import posts

api_router = APIRouter()

api_router.include_router(posts.router, prefix="/posts", tags=["posts"])
