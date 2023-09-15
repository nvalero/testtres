from pydantic import BaseModel

#TODO agregar esta respuesta en 404
class ResponseError(BaseModel):
    correlationId: str
    status: str
    message: str

    def __init__(self, correlationId: str, status: str, message:str) -> None:
        super().__init__(correlationId = correlationId, status = status, message = message)
