from app.models.database import Base
from sqlalchemy import Column,String,Integer
from app.utils.id_generator import generate_id
class Product(Base):
    __tablename__="products"

    id=Column(String(36),primary_key=True,default=generate_id)
    name=Column(String(100),nullable=False,unique=True)
    price=Column(Integer,nullable=False)
    stock_quantity=Column(Integer,nullable=False)