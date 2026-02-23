from app.models.database import Base
from sqlalchemy import Column,String,Float,DateTime,ForeignKey,Integer
from sqlalchemy.orm import relationship
from app.models.database import Base
from datetime import datetime
from app.utils.id_generator import generate_id
class Order(Base):
    __tablename__="orders"

    id=Column(String(40),primary_key=True,default=generate_id)
    user_id=Column(String(40),ForeignKey("users.id"))
    total_amount = Column(Float, nullable=False)
    status = Column(String(20), default="created")
    created_at = Column(DateTime, default=datetime.utcnow)
