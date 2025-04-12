from pydantic import BaseModel

from contact_us.enums import FormOrigin


class ContactUsRequest(BaseModel):
    email: str
    name: str
    message: str
    origin: FormOrigin
    additional_data: dict
    ip: str


class ContactUsResponse(BaseModel):
    email: str
    name: str
    message: str
    origin: FormOrigin
    additional_data: dict
    ip: str

    # retrieve ip on backend
    city: str | None
    country: str | None
