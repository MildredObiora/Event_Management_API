from pydantic import BaseModel, Field
from datetime import datetime

class RegistrationBase(BaseModel):
    user_id: int = Field(..., example=1)
    event_id: int = Field(..., example=1)

class RegistrationCreate(RegistrationBase):
    pass

class Registration(RegistrationBase):
    id: int
    registration_date: datetime = Field(default_factory=datetime.now)
    attended: bool = False

    class Config:
        from_attributes = True