from typing import List

from pydantic import BaseModel

from models.post import PostModel


class GetAllPosts(BaseModel):
    history: List[PostModel]