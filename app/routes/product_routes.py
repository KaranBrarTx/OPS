from fastapi import FastAPI,HTTPException
from schemas.product_schemas import Product
from services.product_services import create_product_data,fetch_product_data
from app.models.database import SessionLocal
from main import app

@app.get('/products/{product_id}')
def fetch_product_data(product_id: str):
    db=SessionLocal()
    try:
        product=fetch_product_data(db,product_id)
        if not product:
            raise HTTPException(status_code=404, detail="Product not found")
        return product
    finally:
        db.close()
@app.post('/products')
def create_user(product: Product):
    db=SessionLocal()
    try:
        return create_product_data(db,product)
    finally:
        db.close()


