from fastapi import APIRouter, HTTPException, status
from schemas.event_schema import Event
from services.event_service import (
    create_event,
    get_event,
    close_event,
    get_all_events,
    get_open_events
)

router = APIRouter(prefix="/events", tags=["Events"])

@router.post("/", response_model=Event, status_code=status.HTTP_201_CREATED)
def add_event(event: Event):
    """Create a new event"""
    return create_event(event.dict())

@router.get("/{event_id}", response_model=Event)
def read_event(event_id: int):
    """Get event details"""
    if event := get_event(event_id):
        return event
    raise HTTPException(status_code=404, detail="Event not found")

@router.get("/", response_model=list[Event])
def list_events(open_only: bool = False):
    """List all events (or only open ones)"""
    return get_open_events() if open_only else get_all_events()

@router.patch("/{event_id}/close")
def close_event_registration(event_id: int):
    """Close event registration"""
    if close_event(event_id):
        return {"message": "Event registration closed"}
    raise HTTPException(status_code=404, detail="Event not found or already closed")