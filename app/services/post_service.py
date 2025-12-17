from typing import List, Optional

from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.post import Post
from app.schemas.post import PostCreate, PostUpdate


class PostService:
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def get_post_by_id(self, post_id: int) -> Optional[Post]:
        result = await self.db_session.execute(select(Post).filter(Post.id == post_id))
        return result.scalars().first()

    async def get_all_posts(self) -> List[Post]:
        result = await self.db_session.execute(select(Post).order_by(Post.id.desc()))
        return list(result.scalars().all())

    async def create_post(self, post: PostCreate) -> Post:
        new_post = Post(title=post.title, content=post.content)
        self.db_session.add(new_post)
        await self.db_session.commit()
        await self.db_session.refresh(new_post)
        return new_post

    async def update_post(self, post_id: int, post_update: PostUpdate) -> Post:
        db_post = await self.get_post_by_id(post_id)
        if not db_post:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Post not found"
            )
        update_data = post_update.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_post, key, value)
        await self.db_session.commit()
        await self.db_session.refresh(db_post)
        return db_post

    async def delete_post(self, post_id: int):
        db_post = await self.get_post_by_id(post_id)
        if not db_post:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Post not found"
            )
        await self.db_session.delete(db_post)
        await self.db_session.commit()
