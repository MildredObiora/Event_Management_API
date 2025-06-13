from data.storage import users
from schemas.user_schema import User
from typing import List, Optional
import uuid

def get_all_users() -> List[User]:
    """Return all active users"""
    return [user for user in users if user.is_active]

def get_user(user_id: int) -> Optional[User]:
    """Get a single user by ID"""
    return next((user for user in users if user.id == user_id and user.is_active), None)

def create_user(user_data: dict) -> User:
    """Create a new user"""
    new_user = User(
        id=len(users) + 1,
        **user_data
    )
    users.append(new_user)
    return new_user

def deactivate_user(user_id: int) -> bool:
    """Deactivate a user (soft delete)"""
    for user in users:
        if user.id == user_id:
            user.is_active = False
            return True
    return False