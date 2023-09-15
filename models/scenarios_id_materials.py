from pydantic import BaseModel
from typing import List


class Result(BaseModel):
    gid: str
    genotype: str
    maturityGroup: str
    category: str
    tech: str
    rm: str

    def __init__(self, gid: str, genotype: str, maturityGroup: str, category: str, tech: str, rm: str = None) -> None:
        super().__init__(gid = gid, genotype = genotype, maturityGroup = maturityGroup, category = category, tech = tech, rm = rm)


class Data(BaseModel):
    results: List[Result]

    def __init__(self, results: List[Result]) -> None:
        super().__init__(results=results)


class ResponseScenariosIdMaterials(BaseModel):
    correlationId: str
    status: str
    message: str
    data: Data

    def __init__(self, correlationId: str, status: str, message:str, data: Data) -> None:
        super().__init__(correlationId = correlationId, status = status, message = message, data = data )
