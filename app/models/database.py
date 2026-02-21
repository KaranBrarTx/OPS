from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base

DATABASE_URL = "mysql+pymysql://sql12817684:WRjtBnNhuP@sql12.freesqldatabase.com:3306/sql12817684"


engine=create_engine(DATABASE_URL,pool_pre_ping=True,pool_recycle=200)

SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)
Base=declarative_base()