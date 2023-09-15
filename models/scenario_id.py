from pydantic import BaseModel
from typing import List
from uuid import UUID


class Filters(BaseModel):
    years: List[str]
    areas: List[str]
    macroregions: List[str]
    microregions: List[str]
    plantingDates: List[str]
    environments: List[str]

    def __init__(self, years: List[str], areas: List[str], macroregions: List[str], microregions: List[str], plantingDates: List[str], environments: List[str]) -> None:
        super().__init__(
            years = years
            ,areas = areas
            ,macroregions = macroregions
            ,microregions = microregions
            ,plantingDates = plantingDates
            ,environments = environments)


class Result(BaseModel):
    id: str
    name: str
    description: str
    country: str
    owner: str
    status: str
    version: int
    location: int
    gid: int
    regions: List[str]
    materials: List[str]
    filters: Filters
    derived: List[str]

    def __init__(self, id: str, name: str, description: str, country: str, owner: str, status: str, version: int, location: int, gid: int, regions: List[str], materials: List[str], filters: Filters, derived: List[str]) -> None:
        super().__init__(
            id = id
            ,name = name
            ,description = description
            ,country = country
            ,owner = owner
            ,status = status
            ,version = version
            ,location = location
            ,gid = gid
            ,regions = regions
            ,materials = materials
            ,filters = filters
            ,derived = derived)


class Data(BaseModel):
    results: List[Result]

    def __init__(self, results: List[Result]) -> None:
        super().__init__(results = results)


class ResponseScenario(BaseModel):
    correlationId: UUID
    status: str
    data: Data

    def __init__(self, correlationId: UUID, status: str, data: Data) -> None:
        super().__init__(correlationId = correlationId
        ,status = status
        ,data = data)
