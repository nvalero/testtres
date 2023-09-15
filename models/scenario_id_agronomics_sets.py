from enum import Enum
from typing import List, Optional
from uuid import UUID
from pydantic import BaseModel, Field


class Result(BaseModel):
    name: str
    available: bool

    def __init__(self, name: str, available: str) -> None:
        super().__init__(name = name, available = available)


class Data(BaseModel):
    results: List[Result]

    def __init__(self, results: List[Result]) -> None:
        super().__init__(results = results)


class ScenarioIdAgronomicsSetsResult(BaseModel):
    correlationId: str
    status: str
    data: Data

    def __init__(self, correlationId: str, status: str, data: Data) -> None:
        super().__init__(correlationId = correlationId, status = status, data = data)
