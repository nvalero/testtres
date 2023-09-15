from pydantic import BaseModel
from typing import Dict


class Result(BaseModel):
    code: int
    description: str
    information: str

    def __init__(self, code: int, description: str, information: str) -> None:
        super().__init__(code = code, description = description, information = information)


class Data(BaseModel):
    results: Dict[str, Result]

    def __init__(self, results: Dict[str, Result]) -> None:
        super().__init__(results = results)


class ThemeValuesIncorrect(BaseModel):
    correlationId: str
    status: str
    data: Data

    def __init__(self, correlationId: str, status: str, data: Data) -> None:
        super().__init__(correlationId = correlationId, status = status, data = data)
