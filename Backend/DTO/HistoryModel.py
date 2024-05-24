from typing import List

from pydantic import BaseModel

from models.history import HistoryModel


class GetAllHistory(BaseModel):
    history: List[HistoryModel]