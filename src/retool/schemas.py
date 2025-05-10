from pydantic import BaseModel, EmailStr, field_validator


class RetoolEmailPayload(BaseModel):
    emails: list[EmailStr]
    subject: str
    body: str

    @field_validator('emails')
    def emails_list_not_empty(cls, v: list[EmailStr]):
        if not v:
            raise ValueError('Emails list cannot be empty')
        return v
