from fastapi import FastAPI
from app.models import user_model, product_model, order_model
from app.models.database import engine, Base
from app.routes import order_routes, product_routes, user_routes
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)  

app.include_router(order_routes.router)
app.include_router(product_routes.router)
app.include_router(user_routes.router)

@app.get('/')
def root():
    return {'message': 'Database Connected'}