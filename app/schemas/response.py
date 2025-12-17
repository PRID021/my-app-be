from typing import Generic, List, Optional, TypeVar

from pydantic import BaseModel

DataType = TypeVar("DataType")


class ResponseWrapper(BaseModel, Generic[DataType]):
    """
    A generic response wrapper for API responses.
    """

    success: bool = True
    data: Optional[DataType] = None
