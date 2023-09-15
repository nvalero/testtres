from uuid import UUID
from pydantic import BaseModel


class Data(BaseModel):
    runId: str

    def __init__(self, runId: str) -> None:
        super().__init__(runId = runId)


class ResponseModelManagerScenariosRun(BaseModel):
    correlationId: str
    status: str
    data: Data

    def __init__(self, correlationId: str, status: str, data: Data) -> None:
        super().__init__(correlationId = correlationId, status = status, data = data )
