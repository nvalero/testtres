from uuid import UUID
from pydantic import BaseModel
from typing import Optional, List


class Measurement(BaseModel):
    gid: int
    genotype: str
    median: str
    minimun: str
    maximum: str
    mode: str
    nluf: str

    def __init__(self, gid: int, genotype: str, median: str, minimun: str, maximum: str, mode: str, nluf: str) -> None:
        super().__init__(gid = gid, genotype = genotype, median = median, minimun = minimun, maximum = maximum, mode = mode, nluf = nluf)


class Result(BaseModel):
    id: int
    rating: str
    measurements: Optional[List[Measurement]]

    def __init__(self, id: int, rating: str, measurements: Optional[List[Measurement]]) -> None:
        super().__init__(id = id, rating = rating, measurements = measurements)


class Data(BaseModel):
    results: Optional[List[Result]]

    def __init__(self, results: Optional[List[Result]]) -> None:
        super().__init__(results = results)


class ResponseScenariosType(BaseModel):
    correlationId: str
    status: str
    message: str
    data: Data

    def __init__(self, correlationId: str, status: str, message: str, data: Data) -> None:
        super().__init__(correlationId = correlationId, status = status, message = message, data = data )
