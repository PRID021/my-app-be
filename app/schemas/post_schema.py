from datetime import datetime

from pydantic import BaseModel, ConfigDict


class PostBase(BaseModel):
    """
    Base schema for a post.
    """

    title: str
    content: str


class PostCreate(PostBase):
    """
    Schema for creating a post.
    """

    pass


class PostRead(PostBase):
    """
    Schema for reading a post.
    """

    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
