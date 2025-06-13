from fastapi import APIRouter, HTTPException, status
from schemas.user_schema import User
from services.user_service import (
    create_user,
    get_user,
    deactivate_user,
    get_all_users
)

router = APIRouter()

@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
def register_user(user: User):
    """Create a new user"""
    return create_user(user.model_dump())

@router.get("/{user_id}", response_model=User)
def read_user(user_id: int):
    """Get a specific user"""
    if user := get_user(user_id):
        return user
    raise HTTPException(status_code=404, detail="User not found")

@router.get("/", response_model=list[User])
def list_users():
    """List all active users"""
    return get_all_users()

@router.patch("/{user_id}/deactivate")
def deactivate_user_account(user_id: int):
    """Deactivate a user (soft delete)"""
    if deactivate_user(user_id):
        return {"message": "User deactivated"}
    raise HTTPException(status_code=404, detail="User not found")