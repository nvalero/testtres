from typing import Optional, List
from pydantic import BaseModel


class Region(BaseModel):
    id: int
    name: str
    parent: int

    def __init__(self, id: int, name: str, parent: int) -> None:
        super().__init__(id = id, name = name, parent = parent)


class Results(BaseModel):
    sub_region: List[Region]
    macro_region: List[Region]

    def __init__(self, sub_region: List[Region], macro_region: List[Region]) -> None:
        super().__init__(sub_region = sub_region, macro_region = macro_region)


class Data(BaseModel):
    results: Results

    def __init__(self, results: Results) -> None:
        super().__init__(results = results)


class ThemeValuesMacroRegion(BaseModel):
    correlationId: str
    status: str
    data: Data

    def __init__(self, correlationId: str, status: str, data: Data) -> None:
        super().__init__(correlationId = correlationId, status = status, data = data)
