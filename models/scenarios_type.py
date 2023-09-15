from uuid import UUID
from pydantic import BaseModel
from typing import Optional, List


class Data(BaseModel):
    idScenario: UUID

    def __init__(self, idScenario: UUID) -> None:
        super().__init__(idScenario = idScenario)


class ResponseScenariosType(BaseModel):
    correlationId: str
    status: str
    message: str
    data: Data

    def __init__(self, correlationId: str, status: str, message: str, data: Data) -> None:
        super().__init__(correlationId = correlationId, status = status, message = message, data = data )
