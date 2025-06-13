from fastapi import APIRouter, HTTPException
from schemas.speaker_schema import Speaker
from services.speaker_service import (
    get_all_speakers,
    add_speaker
)

router = APIRouter(prefix="/speakers", tags=["Speakers"])

@router.get("/", response_model=list[Speaker])
def list_speakers():
    """List all speakers"""
    return get_all_speakers()

@router.get("/{speaker_id}", response_model=Speaker)
def read_speaker(speaker_id: int):
    """Get speaker details"""
    if speaker := read_speaker(speaker_id):
        return speaker
    raise HTTPException(status_code=404, detail="Speaker not found")

@router.post("/", response_model=Speaker, status_code=201)
def create_speaker(speaker: Speaker):
    """Add a new speaker (beyond the 3 initial ones)"""
    return add_speaker(speaker.model_dump())