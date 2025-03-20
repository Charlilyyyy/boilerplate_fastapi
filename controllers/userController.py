from fastapi import APIRouter, HTTPException
from models import User, UserCreate
from services.userService import fetch_all_users, fetch_user, add_user, modify_user, remove_user

router = APIRouter()

# Get all users
@router.get("/users/", response_model=list[User])
def get_users():
    return fetch_all_users()

# Get a single user
@router.get("/users/{user_id}", response_model=User)
def get_user(user_id: int):
    user = fetch_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# Create a new user
@router.post("/users/", response_model=User)
def create_user(user: UserCreate):
    return add_user(user.dict())

# Update a user
@router.put("/users/{user_id}", response_model=User)
def update_user(user_id: int, user: UserCreate):
    updated_user = modify_user(user_id, user.dict())
    if not updated_user:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user

# Delete a user
@router.delete("/users/{user_id}")
def delete_user(user_id: int):
    if not remove_user(user_id):
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted"}
