from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class EventBase(BaseModel):
    title: str = Field(..., example="Karatu 2024 Graduation ceremony")
    location: str = Field(..., example="Lagos")
    date: datetime = Field(..., example="2025-05-15T09:30:00")

class EventCreate(EventBase):
    pass

class Event(EventBase):
    id: int
    is_open: bool = True
    created_at: datetime = Field(default_factory=datetime.now)

    class Config:
        from_attributes = True