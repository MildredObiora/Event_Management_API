from data.storage import events
from schemas.event_schema import Event
from typing import List, Optional

def create_event(event_data: dict) -> Event:
    """Create a new event"""
    new_event = Event(
        id=len(events) + 1,
        **event_data
    )
    events.append(new_event)
    return new_event

def get_event(event_id: int) -> Optional[Event]:
    """Get single event by ID"""
    return next((event for event in events if event.id == event_id), None)

def get_all_events() -> List[Event]:
    """Get all events"""
    return events

def get_open_events() -> List[Event]:
    """Get only events accepting registrations"""
    return [event for event in events if event.is_open]

def close_event(event_id: int) -> bool:
    """Close event registration"""
    for event in events:
        if event.id == event_id:
            event.is_open = False
            return True
    return False