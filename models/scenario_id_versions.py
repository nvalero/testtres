from enum import Enum
from typing import List, Optional
from uuid import UUID
from pydantic import BaseModel, Field


class Result(BaseModel):
    id: str
    version: str
    user: str
    date: str
    error: str

    def __init__(self, id: str, version: str, user: str, date: str, error: str) -> None:
        super().__init__(id=id, version=version, user=user, date=date, error=error)


class Data(BaseModel):
    results: List[Result]

    def __init__(self, results: List[Result]) -> None:
        super().__init__(results = results)


class ScenarioIdVersionsResult(BaseModel):
    correlation_id: str
    status: str
    data: Data

    def __init__(self, correlation_id: str, status: str, data: Data) -> None:
        super().__init__(correlation_id = correlation_id, status = status, data = data)
