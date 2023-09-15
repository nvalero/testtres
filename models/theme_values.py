from typing import Optional, List
from pydantic import BaseModel

class Area(BaseModel):
    id: int
    name: str

    def __init__(self, id: int, name: str) -> None:
        super().__init__(id = id, name = name)


class Region(BaseModel):
    id: int
    name: str
    parent: int

    def __init__(self, id: int, name: str, parent: int) -> None:
        super().__init__(id = id, name = name, parent = parent)


class Results(BaseModel):
    area: List[Area]
    sub_region: List[Region]
    macro_region: List[Region]
    scenario_environment: Optional[List[Area]] | None = None
    scenario_planting_date: Optional[List[Area]] | None = None
    scenario_year: Optional[List[Area]] | None = None

    def __init__(self, area: List[Area], sub_region: List[Region], macro_region: List[Region], scenario_environment: Optional[List[Area]] = None,
                 scenario_planting_date: Optional[List[Area]] = None, scenario_year: Optional[List[Area]] = None) -> None:
        super().__init__(area = area, sub_region = sub_region, macro_region = macro_region,
                         scenario_environment = scenario_environment, scenario_planting_date = scenario_planting_date,
                         scenario_year = scenario_year)


class Data(BaseModel):
    results: Results

    def __init__(self, results: Results) -> None:
        super().__init__(results = results)


class ThemeValues(BaseModel):
    correlationId: str
    status: str
    data: Data

    def __init__(self, correlationId: str, status: str, data: Data) -> None:
        super().__init__(correlationId = correlationId, status = status, data = data)
