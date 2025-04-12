from pydantic import BaseModel


class Main(BaseModel):
    success: bool
    service: str
    request_metadata: dict


class LocationIP(BaseModel):
    ip: str
    city: str | None
    country: str | None
