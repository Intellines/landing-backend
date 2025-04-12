from pydantic import BaseModel


class Main(BaseModel):
    success: bool
    service: str
    request_metadata: dict
