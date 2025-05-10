from pydantic import BaseModel, EmailStr, constr

from contact_us.enums import FormOrigin
from all_enums import Origin


class ContactUsRequest(BaseModel):
    email: EmailStr
    name: constr(min_length=1)
    message: str | None
    origin: FormOrigin
    additional_data: dict
    ip: str | None


class ContactUsResponse(BaseModel):
    email: EmailStr
    name: constr(min_length=1)
    message: str | None
    origin: FormOrigin
    additional_data: dict
    ip: str | None

    city: str | None = None
    country: str | None = None


class ContactUsLeadCreate(BaseModel):
    name: constr(max_length=500)
    email: str
    name: str
    message: str | None
    origin: Origin = Origin.LANDING
    ip: str | None
    country: str | None
    city: str | None
    additional_data: dict = {}
