from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field

from models.checkIn import PyObjectId


class HistoryModel(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    date: datetime = Field(...)
    total: int = Field(...)
    new: int = Field(...)

