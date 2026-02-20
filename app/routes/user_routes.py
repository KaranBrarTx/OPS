from fastapi import FastAPI,HTTPException
app=FastAPI()
from schemas.user_schemas import User
from services.user_services import fetch_user_data,load_data,create_user_data
@app.get('/user/{user_id}')
def get_user_data(user_id:str):
    user=fetch_user_data(user_id)

    if not user:
        raise HTTPException(status_code=404, detail="User not found !")
    return user
@app.post('/user/{user_id}')
def create_user(user: User):
    create_user_data(user)