from datetime import datetime

from sqlmodel import Field, SQLModel


class User(SQLModel, table=True):
    __tablename__ = 'users'
    id: int = Field(primary_key=True)
    username: str = Field(unique=True, max_length=255)
    email: str = Field(unique=True, max_length=320)
    password_hash: str = Field(max_length=256)
    is_disabled: bool = False
    updated_at: datetime = Field(default_factory=datetime.now)
    created_at: datetime = Field(default_factory=datetime.now)
