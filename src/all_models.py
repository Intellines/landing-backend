from datetime import datetime

from sqlmodel import SQLModel, Field
from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import JSONB

from src.all_enums import Origin


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


class User(SQLModel, table=True):
    __tablename__ = 'users'
    id: int = Field(primary_key=True)
    username: str = Field(unique=True, max_length=255)
    email: str = Field(unique=True, max_length=320)
    password_hash: str = Field(max_length=256)
    is_disabled: bool = False
    updated_at: datetime = Field(default_factory=datetime.now)
    created_at: datetime = Field(default_factory=datetime.now)
