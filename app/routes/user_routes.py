from fastapi import FastAPI,HTTPException
from fastapi import APIRouter

router = APIRouter()
from app.schemas.user_schemas import User
from app.services.user_services import create_user_data,fetch_user_data
from app.models.database import SessionLocal
@router.get("/users/{user_id}")
def fetch_user(user_id: str):
    db=SessionLocal()
    try:
        user=fetch_user_data(db,user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user
    finally:
        db.close()
@router.post("/users")
def create_user(user: User):
    db=SessionLocal()
    try:
        return create_user_data(db,user)
    finally:
        db.close()
from app.services.user_services import fetch_all_data
@router.get('/users')
def fetch_all_user():
    db=SessionLocal()
    try:
        users=fetch_all_data(db,User)
        return users
    finally:
        db.close()