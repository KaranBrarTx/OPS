from fastapi import FastAPI,HTTPException
app=FastAPI()
from schemas.user_schemas import User
from services.user_services import create_user_data,fetch_user_data
from app.models.database import SessionLocal
@app.get("/user/{user_id}")
def fetch_user(user_id: str):
    db=SessionLocal()
    try:
        user=fetch_user_data(db,user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user
    finally:
        db.close()
@app.post("/users")
def create_user(user: User):
    db=SessionLocal()
    try:
        return create_user_data(db,user)
    finally:
        db.close()