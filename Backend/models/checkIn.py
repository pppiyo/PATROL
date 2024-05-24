from datetime import datetime
from typing import Optional, List, Annotated

from pydantic import BaseModel, Field, ConfigDict, BeforeValidator

PyObjectId = Annotated[str, BeforeValidator(str)]


class CheckInModel(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    userId: str = Field(...)
    lat: float = Field(...)
    lng: float = Field(...)
    createdAt: datetime = Field(default_factory=datetime.utcnow)


class CheckInCollection(BaseModel):
    checkIns: List[CheckInModel]
