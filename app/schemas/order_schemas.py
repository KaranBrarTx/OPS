# from datetime import datetime
# from pydantic import BaseModel

# class Order(BaseModel):
#     id: str
#     user_id: str
#     total_amount: int
#     status: str
#     created_at: datetime


from datetime import datetime
from pydantic import BaseModel
from typing import Any, List


class OrderItem(BaseModel):
    product_id: str
    quantity: int


class Order(BaseModel):
    user_id: str
    items: List[OrderItem]


class OrderResponse(BaseModel):
    id: str
    user_id: str
    products: Any          
    total_amount: float    
    status: str
    created_at: datetime

    class Config:
        from_attributes = True  