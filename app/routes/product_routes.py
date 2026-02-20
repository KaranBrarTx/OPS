from fastapi import FastAPI,HTTPException
from schemas.product_schemas import Product
app=FastAPI()

@app.get('/products/{product_id}')
def fetch_product_data(product_id: str):
    pass


