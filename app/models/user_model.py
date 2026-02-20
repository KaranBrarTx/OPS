from app.models.database import Base
from sqlalchemy import Column,String


class User(Base):
    __tablename__="users"

    id=Column(String(30),primary_key=True)
    name=Column(String(100),nullable=False)
    email=Column(String(100),unique=True,nullable=False)






