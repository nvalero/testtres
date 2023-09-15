from uuid import UUID
from pydantic import BaseModel
from typing import List

class Result(BaseModel):
    code: str
    description: str
    information: str

    def __init__(self, code: str, description: str, information: str) -> None:
        super().__init__(code = code, description = description, information = information)


class Data(BaseModel):
    errors: List[Result]

    def __init__(self, results: List[Result]) -> None:
        super().__init__(results = results)

#TODO agregar esta respuesta en 404
class ResponseError(BaseModel):
    correlationId: str
    status: str
    message: str
    data: Data

    def __init__(self, correlationId: str, status: str, message:str, data: Data) -> None:
        super().__init__(correlationId = correlationId, status = status, message = message, data = data)
