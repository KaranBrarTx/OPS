from app.models.database import Base
from sqlalchemy import Column,String,Integer

class Product(Base):
    __tablename__="products"

    id=Column(String(30),primary_key=True)
    name=Column(String(100),nullable=False,unique=True)
    price=Column(Integer,nullable=False)
    stock_quantity=Column(Integer,nullable=False)