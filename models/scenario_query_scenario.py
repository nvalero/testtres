from enum import Enum
from typing import List, Optional
from uuid import UUID


class Area(Enum):
    DEVELOPMENT = "Development"
    RESEARCH = "Research"


class PlantingDate(Enum):
    EARLY = "Early"
    LATE = "Late"
    MEDIUM = "Medium"
    N_A = "N/A"


class Filters(BaseModel):
    years: List[int]
    areas: List[Area]
    macroregions: List[str]
    microregions: List[str]
    planting_dates: List[PlantingDate]
    environments: List[str]

    def __init__(self, years: List[int], areas: List[Area], macroregions: List[str], microregions: List[str], planting_dates: List[PlantingDate], environments: List[str]) -> None:
        super().__init__(years = years, areas = areas, macroregions = macroregions, microregions = microregions, planting_dates = planting_dates, environments = environments)


class Result(BaseModel):
    id: UUID
    name: str
    description: str
    country: int
    owner: str
    status: str
    version: int
    location: int
    gid: int
    regions: Optional[List[int]]
    materials: Optional[List[int]]
    filters: Filters
    derived: Optional[List['Result']]

    def __init__(self, id: UUID, name: str, description: str, country: int, owner: str, status: str, version: int, location: int, gid: int, regions: Optional[List[int]], materials: Optional[List[int]], filters: Filters, derived: Optional[List['Result']]) -> None:
        super().__init__(id = id, name = name, description = description, country = country, owner = owner, status = status, version = version, location = location,
                         gid = gid, regions = regions, materials = materials, filters = filters, derived = derived)


class Data(BaseModel):
    results: List[Result]

    def __init__(self, results: List[Result]) -> None:
        super().__init__(results = results)


class ScenarioQueryScenarioResult(BaseModel):
    correlation_id: str
    status: str
    data: Data

    def __init__(self, correlation_id: str, status: str, data: Data) -> None:
        super().__init__(correlation_id = correlation_id, status = status, data = data)
