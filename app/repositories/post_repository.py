from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.post import Post
from app.schemas.post_schema import PostCreate


class PostRepository:
    """
    Repository for post-related database operations.
    """
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def create_post(self, post: PostCreate) -> Post:
        """
        Create a new post in the database.
        """
        db_post = Post(title=post.title, content=post.content)
        self.db_session.add(db_post)
        await self.db_session.commit()
        await self.db_session.refresh(db_post)
        return db_post

    async def get_posts(self) -> list[Post]:
        """
        Get all posts from the database.
        """
        result = await self.db_session.execute(select(Post).order_by(Post.created_at.desc()))
        return result.scalars().all()
