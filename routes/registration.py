from fastapi import APIRouter, HTTPException, status
from schemas.registration_schema import Registration
from services.registration_service import (
    register_for_event,
    mark_attendance,
    get_user_registrations,
    get_event_attendees
)

router = APIRouter(prefix="/registrations", tags=["Registrations"])

@router.post("/", response_model=Registration, status_code=status.HTTP_201_CREATED)
def register_user_for_event(registration: Registration):
    """Register a user for an event"""
    if result := register_for_event(registration.dict()):
        return result
    raise HTTPException(
        status_code=400,
        detail="Registration failed (user inactive, event closed, or duplicate)"
    )

@router.get("/user/{user_id}", response_model=list[Registration])
def list_user_registrations(user_id: int):
    """Get all registrations for a user"""
    return get_user_registrations(user_id)

@router.patch("/{reg_id}/attend")
def confirm_attendance(reg_id: int):
    """Mark a user as attended"""
    if mark_attendance(reg_id):
        return {"message": "Attendance confirmed"}
    raise HTTPException(status_code=404, detail="Registration not found")

@router.get("/event/{event_id}/attendees")
def list_event_attendees(event_id: int, attended_only: bool = False):
    """List all registrations for an event (optionally only attendees)"""
    return get_event_attendees(event_id, attended_only)