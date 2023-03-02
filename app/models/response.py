from pydantic import BaseModel
from datetime import datetime, date
from typing import Optional

class Strategy(BaseModel):
    creater_id: str
    created_date: date
    assignemnt: list[int]

class StrategyList(BaseModel):
    strategies: list[Strategy]

class MyResult(BaseModel):
    my_strategy: Strategy
    opponent_strategy: Strategy

class MyResultList(BaseModel):
    my_results: list[MyResult]
