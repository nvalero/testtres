from pydantic import BaseModel
from typing import List


class Data(BaseModel):
    results: List[str]

    def __init__(self, results: List[str]) -> None:
        super().__init__(results=results)


class ResponseScenariosMaterials(BaseModel):
    correlationId: str
    status: str
    data: Data

    def __init__(self, correlationId: str, status: str, data: Data) -> None:
        super().__init__(correlationId = correlationId, status = status, data = data )
