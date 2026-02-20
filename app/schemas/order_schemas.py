from datetime import datetime
from pydantic import BaseModel

class Order(BaseModel):
    id: str
    user_id: str
    total_amount: int
    status: str
    created_at: datetime