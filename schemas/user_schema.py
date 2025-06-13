from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime

class UserBase(BaseModel):
    name: str = Field(..., example="Jane Doe")
    email: EmailStr = Field(..., example="jane@example.com")

class UserCreate(UserBase):
    pass  # Additional fields for creation if needed

class User(UserBase):
    id: int
    is_active: bool = True
    created_at: datetime = Field(default_factory=datetime.now)

    class Config:
        from_attributes = True