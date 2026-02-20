from pydantic import BaseModel,Field,EmailStr
class User(BaseModel):
    id: str
    name: str
    email: EmailStr