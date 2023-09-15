from datetime import datetime
from typing import List
from pydantic import BaseModel


class Value(BaseModel):
    material: str
    genotype: str
    value: str

    def __init__(self, material: str, genotype: str, value: str) -> None:
        super().__init__(material = material, genotype = genotype, value = value)


class Result(BaseModel):
    user: str
    account: str
    region: str
    date: datetime
    selected: bool
    values: List[Value]
    new: bool

    def __init__(self, user: str, account: str, region: str, date: datetime, selected: bool, values: List[Value], new: bool) -> None:
        super().__init__(user = user, account = account, region = region, date = date, selected = selected, values = values, new = new)


class Data(BaseModel):
    results: List[Result]

    def __init__(self, results: List[Result]) -> None:
        super().__init__(results = results)


class ResponseAgronomicsRun(BaseModel):
    correlation_id: str
    status: str
    data: Data

    def __init__(self, correlation_id: str, status: str, data: Data) -> None:
        super().__init__(correlation_id = correlation_id, status = status, data = data)
