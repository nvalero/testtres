from pydantic import BaseModel
from typing import Optional

#no estoy segura de esta estructura, por si falla, se puede revisar
class Result(BaseModel):
    pass

    def __init__(self, ) -> None:
        pass


class Data(BaseModel):
    results: Result

    def __init__(self, results: Result) -> None:
        super().__init__(results = results)


class ResponseError(BaseModel):
    correlationId: str
    status: str
    data: Data

    def __init__(self, correlationId: str, status: str, data: Data) -> None:
        super().__init__(correlationId = correlationId, status = status, data = data)
