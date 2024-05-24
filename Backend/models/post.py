from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field

from models.checkIn import PyObjectId


class PostModel(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    createdAt: datetime = Field(default_factory=datetime.utcnow)
    post: str = Field(...)
