from fastapi import FastAPI,HTTPException
from app.schemas.product_schemas import Product
from app.services.product_services import create_product_data,fetch_product_data,fetch_all_products_data
from app.models.database import SessionLocal
from fastapi import APIRouter

router = APIRouter()

@router.get('/products/{product_id}')
def get_product(product_id: str):
    db=SessionLocal()
    try:
        product=fetch_product_data(db,product_id)
        if not product:
            raise HTTPException(status_code=404, detail="Product not found")
        return product
    finally:
        db.close()
@router.post('/products')
def create_product(product: Product):
    db=SessionLocal()
    try:
        return create_product_data(db,product)
    finally:
        db.close()


