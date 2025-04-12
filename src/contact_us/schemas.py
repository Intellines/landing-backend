from pydantic import BaseModel
from contact_us.enums import FormOrigin


class ContactUsRequest(BaseModel):
    email: str
    name: str
    message: str
    origin: FormOrigin
    additional_data: dict


class ContactUsResponse(BaseModel):
    email: str
    name: str
    message: str
    origin: FormOrigin
    additional_data: dict

    # retrieve ip on backend
    ip: str | None
