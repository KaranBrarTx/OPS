from pydantic import BaseModel,Field
class Product(BaseModel):
    id:str
    name: str
    price: int
    stock_quantity: int
    