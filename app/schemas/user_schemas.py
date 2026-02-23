from pydantic import BaseModel,Field,EmailStr
from typing import Optional
class User(BaseModel):
    id: Optional[str]=None
    name: str
    email: EmailStr