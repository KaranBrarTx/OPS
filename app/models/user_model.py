from app.models.database import Base
from sqlalchemy import Column,String
from app.utils.id_generator import generate_id
class User(Base):
    __tablename__="users"

    id=Column(String(36),primary_key=True,default=generate_id)
    name=Column(String(100),nullable=False)
    email=Column(String(100),unique=True,nullable=False)






