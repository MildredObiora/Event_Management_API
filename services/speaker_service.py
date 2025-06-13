from data.storage import speakers
from schemas.speaker_schema import Speaker
from typing import List, Optional

def get_all_speakers() -> List[Speaker]:
    """List all speakers"""
    return speakers

def get_speaker_by_id(speaker_id: int) -> Optional[Speaker]:
    """Get speaker by ID"""
    return next((speaker for speaker in speakers if speaker.id == speaker_id), None)

def add_speaker(speaker_data: dict) -> Speaker:
    """Add a new speaker"""
    new_speaker = Speaker(
        id=len(speakers) + 1,
        **speaker_data
    )
    speakers.append(new_speaker)
    return new_speaker