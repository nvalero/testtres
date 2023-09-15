from typing import List
from pydantic import BaseModel, Field


class Result(BaseModel):
    id: int
    year: int
    area: str
    macroregion: str
    microregion: str
    plantingDate: str
    environment: str
    testId: str
    testNumber: int
    location: str
    testType: str

    def __init__(self, id: int, year: int, area: str, macroregion: str, microregion: str, plantingDate: str, environment: str, testId: str, testNumber: int, location: str, testType: str) -> None:
        super().__init__(id = id, year = year, area = area, macroregion = macroregion, microregion = microregion, plantingDate = plantingDate, environment = environment, testId = testId,
                         testNumber = testNumber, location = location, testType = testType)


class Data(BaseModel):
    results: List[Result]

    def __init__(self, results: List[Result]) -> None:
        super().__init__(results = results)


class ScenarioQueryRegionsResult(BaseModel):
    correlationId: str
    status: str
    data: Data

    def __init__(self, correlationId: str, status: str, data: Data) -> None:
        super().__init__(correlationId = correlationId, status = status, data = data)
