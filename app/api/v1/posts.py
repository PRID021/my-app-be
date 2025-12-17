from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.logger import logger
from app.db.session import get_db
from app.schemas.post import Post as PostSchema
from app.schemas.post import PostCreate
from app.services.post_service import PostService

router = APIRouter()


@router.post("/", response_model=PostSchema, status_code=status.HTTP_201_CREATED)
async def create_new_post(post_in: PostCreate, db: AsyncSession = Depends(get_db)):
    """
    Create a new post.
    """
    logger.info("Received request to create a new post", title=post_in.title)
    service = PostService(db)
    created_post = await service.create_post(post_in)
    logger.info("Successfully created new post", post_id=created_post.id)
    return created_post


@router.get("/", response_model=List[PostSchema])
async def get_all_posts(db: AsyncSession = Depends(get_db)):
    """
    Get all posts.
    """
    logger.info("Received request to get all posts")
    service = PostService(db)
    posts = await service.get_all_posts()
    logger.info(f"Found {len(posts)} posts", count=len(posts))
    return posts
