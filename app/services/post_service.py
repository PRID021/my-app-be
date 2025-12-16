from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.post_repository import PostRepository
from app.schemas.post_schema import PostCreate
from app.models.post import Post


class PostService:
    """
    Service for post-related business logic.
    """
    def __init__(self, db_session: AsyncSession):
        self.repo = PostRepository(db_session)

    async def create_post(self, post: PostCreate) -> Post:
        """
        Create a new post.
        """
        # In a real application, you might have more business logic here,
        # like sending notifications, checking for duplicates, etc.
        return await self.repo.create_post(post)

    async def get_all_posts(self) -> list[Post]:
        """
        Get all posts.
        """
        return await self.repo.get_posts()
