from datetime import datetime, timezone

from sqlmodel import SQLModel, Field
from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import JSONB

from src.enums import Origin


class ContactUsFormLeads(SQLModel, table=True):
    __tablename__ = "contact_us_form_leads"

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
    updated_at: datetime | None = Field(default_factory=lambda: datetime.now(timezone.utc))
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
