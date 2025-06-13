from data.storage import registrations, users, events
from schemas.registration_schema import Registration
from typing import List, Optional
from datetime import datetime

def register_for_event(registration_data: dict) -> Optional[Registration]:
    """Register a user for an event with validation"""
    user = next((u for u in users if u.id == registration_data["user_id"] and u.is_active), None)
    event = next((e for e in events if e.id == registration_data["event_id"] and e.is_open), None)
    
    # Validate
    if not user or not event:
        return None
        
    # Check for existing registration
    if any(r.user_id == user.id and r.event_id == event.id for r in registrations):
        return None
        
    # Create registration
    new_reg = Registration(
        id=len(registrations) + 1,
        **registration_data
    )
    registrations.append(new_reg)
    return new_reg

def get_user_registrations(user_id: int) -> List[Registration]:
    """Get all registrations for a user"""
    return [r for r in registrations if r.user_id == user_id]

def mark_attendance(registration_id: int) -> bool:
    """Mark a registration as attended"""
    for reg in registrations:
        if reg.id == registration_id:
            reg.attended = True
            return True
    return False

def get_event_attendees(event_id: int, attended_only: bool = False) -> List[Registration]:
    """Get registrations for an event"""
    registrations = [r for r in registrations if r.event_id == event_id]
    if attended_only:
        return [r for r in registrations if r.attended]
    return registrations