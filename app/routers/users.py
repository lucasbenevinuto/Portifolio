from fastapi import APIRouter, HTTPException
from typing import List
from app.schemas.user import User, UserCreate, UserUpdate

router = APIRouter()

# Simulação de banco de dados
users_db = []

@router.get("/", response_model=List[User])
async def read_users():
    return users_db

@router.post("/", response_model=User)
async def create_user(user: UserCreate):
    new_user = User(id=len(users_db) + 1, **user.dict())
    users_db.append(new_user)
    return new_user

@router.get("/{user_id}", response_model=User)
async def read_user(user_id: int):
    for user in users_db:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")

@router.put("/{user_id}", response_model=User)
async def update_user(user_id: int, user: UserUpdate):
    for i, stored_user in enumerate(users_db):
        if stored_user.id == user_id:
            update_data = user.dict(exclude_unset=True)
            updated_user = stored_user.copy(update=update_data)
            users_db[i] = updated_user
            return updated_user
    raise HTTPException(status_code=404, detail="User not found")

@router.delete("/{user_id}")
async def delete_user(user_id: int):
    for i, user in enumerate(users_db):
        if user.id == user_id:
            users_db.pop(i)
            return {"message": "User deleted successfully"}
    raise HTTPException(status_code=404, detail="User not found") 