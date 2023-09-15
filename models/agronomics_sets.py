from uuid import UUID
from pydantic import BaseModel


class Data(BaseModel):
    idAgronomicSet: UUID

    def __init__(self, idAgronomicSet: UUID) -> None:
        super().__init__(idAgronomicSet = idAgronomicSet)


class ResponseAgronomicSet(BaseModel):
    correlationId: str
    status: str
    message: str
    data: Data

    def __init__(self, correlationId: str, status: str, message: str, data: Data) -> None:
        super().__init__(correlationId = correlationId, status = status, message = message, data = data )
