from typing import List
from pydantic import BaseModel


class Result(BaseModel):
    report: str
    token: str

    def __init__(self, report: str, token: str) -> None:
        super().__init__(report = report, token = token)


class Data(BaseModel):
    results: List[Result]

    def __init__(self, results: List[Result]) -> None:
        super().__init__(results = results)


class ResultGraphsEmbedded(BaseModel):
    correlation_id: str
    status: str
    data: Data

    def __init__(self, correlation_id: str, status: str, data: Data) -> None:
        super().__init__(correlation_id = correlation_id, status = status, data = data)
