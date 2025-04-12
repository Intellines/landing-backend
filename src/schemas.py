from pydantic import BaseModel


class MainResponse(BaseModel):
    success: bool
    service: str
    ip: str


class LocationIP(BaseModel):
    ip: str
    city: str | None
    country: str | None
