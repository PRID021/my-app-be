from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db
from app.schemas.post_schema import PostCreate, PostRead
from app.services.post_service import PostService
from app.core.logger import logger

router = APIRouter()


@router.post("/", response_model=PostRead, status_code=status.HTTP_201_CREATED)
async def create_new_post(post: PostCreate, db: AsyncSession = Depends(get_db)):
    """
    Create a new post.
    """
    logger.info("Received request to create a new post", title=post.title)
    service = PostService(db)
    created_post = await service.create_post(post)
    logger.info("Successfully created new post", post_id=created_post.id)
    return created_post


@router.get("/", response_model=List[PostRead])
async def get_all_posts(db: AsyncSession = Depends(get_db)):
    """
    Get all posts.
    """
    logger.info("Received request to get all posts")
    service = PostService(db)
    posts = await service.get_all_posts()
    logger.info(f"Found {len(posts)} posts")
    return posts
