from fastapi import FastAPI
from app.models import user_model,product_model,order_model
from app.models.database import engine,Base
from app.routes import order_routes,product_routes,user_routes
app=FastAPI()
Base.metadata.create_all(bind=engine)
import app.routes.user_routes
import app.routes.product_routes
import app.routes.order_routes
@app.get('/')
def root():
    return {'message':'Database Connected'}
