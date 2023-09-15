from uuid import UUID
from pydantic import BaseModel
from typing import List

class Result(BaseModel):
    code: str
    description: str
    information: str

    def __init__(self, code: str, description: str, information: str) -> None:
        super().__init__(code = code, description = description, information = information)


class ResponseError(BaseModel):
    correlationId: str
    status: str
    message: str
    errors: List[Result]

    def __init__(self, correlationId: str, status: str, message:str, errors: List[Result]) -> None:
        super().__init__(correlationId = correlationId, status = status, message = message, errors = errors)
