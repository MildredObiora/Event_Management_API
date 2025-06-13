from pydantic import BaseModel, Field

class SpeakerBase(BaseModel):
    name: str = Field(..., example="Ms. Tabitha kayvu")
    topic: str = Field(..., example="Getting into Tech")

class SpeakerCreate(SpeakerBase):
    pass

class Speaker(SpeakerBase):
    id: int

    class Config:
        from_attributes = True