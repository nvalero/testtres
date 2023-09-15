from typing import List
from pydantic import BaseModel, Field

class Results(BaseModel):
    id: int
    name: str

    def __init__(self, id: int, name: str) -> None:
        super().__init__(id = id, name = name, parent = parent)


class Data(BaseModel):
    results: Results

    def __init__(self, results: Results) -> None:
        super().__init__(results = results)


class ThemePath(BaseModel):
    correlationId: str
    status: str
    data: Data

    def __init__(self, correlationId: str, status: str, data: Data) -> None:
        super().__init__(correlationId = correlationId, status = status, data = data)
