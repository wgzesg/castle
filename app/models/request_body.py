from pydantic import BaseModel
from datetime import datetime, date
from typing import Optional

class CreateNewStrategy(BaseModel):
    creater_id: str
    created_date: date
    assignemnt: list[int]

class QueryMyStrategy(BaseModel):
    user_id: str
    from_date: Optional[date]
    to_date: Optional[date]

class QueryMyResult(BaseModel):
    user_id: str
    from_date: Optional[date]
    to_date: Optional[date]


