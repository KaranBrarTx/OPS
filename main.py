from fastapi import FastAPI
from app.models import user_model,product_model,order_model
from app.models.database import engine,Base
from app.routes import order_routes, product_routes, user_routes
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(order_routes.router)
app.include_router(product_routes.router)
app.include_router(user_routes.router)
@app.get('/')
def root():
    return {'message':'Database Connected'}
