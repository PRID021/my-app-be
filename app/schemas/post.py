from datetime import datetime

from pydantic import BaseModel, ConfigDict


class PostBase(BaseModel):
    """
    Base schema for a post with shared properties.
    """

    title: str
    content: str


class PostCreate(PostBase):
    """
    Schema for creating a post via the API.
    """

    pass


class PostUpdate(BaseModel):
    """
    Schema for updating a post, all fields are optional.
    """

    title: Optional[str] = None
    content: Optional[str] = None


class Post(PostBase):
    """
    Schema for returning a post to the client.
    """

    id: int
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)
