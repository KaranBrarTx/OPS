from fastapi import FastAPI
from app.models import user_model,product_model,order_model
from app.models.database import engine,Base

app=FastAPI()
Base.metadata.create_all(bind=engine)

@app.get('/')
def root():
    return {'message':'Database Connected'}
