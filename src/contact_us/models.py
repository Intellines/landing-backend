from datetime import datetime

from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import JSONB
from sqlmodel import Field, SQLModel

from enums import Origin


class ContactUsFormLeads(SQLModel, table=True):
    __tablename__ = 'contact_us_form_leads'

    id: int = Field(primary_key=True)
    name: str = Field(max_length=500, unique=True)
    email: str
    name: str
    message: str | None
    origin: Origin = Field(default=Origin.LANDING)
    ip: str | None
    country: str | None
    city: str | None
    additional_data: dict = Field(default={}, sa_column=Column(JSONB))
    updated_at: datetime | None = Field(default_factory=datetime.now)
    created_at: datetime = Field(default_factory=datetime.now)
