from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# for connection string 
DATABASE_URL = "postgresql://postgres:1234@localhost/fastapi_db"

engine = create_engine(DATABASE_URL)  # Database se connect karta hai
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)  # 
Base = declarative_base()  # for Models  base class