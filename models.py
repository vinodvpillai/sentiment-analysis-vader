from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Create SQLAlchemy engine
SQLALCHEMY_DATABASE_URL = os.getenv('DATABASE_URL')
engine = create_engine(SQLALCHEMY_DATABASE_URL)
# Create SQLAlchemy session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Define Rating table
class Rating(Base):
    __tablename__ = "ratings"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer)
    customer_id = Column(Integer)
    location_id = Column(Integer)
    order_id = Column(Integer)
    star_rating = Column(Integer)
    created_at = Column(DateTime)
    review = Column(String)
    score = Column(Float)
    
# Create tables in the database if not exist
Base.metadata.create_all(bind=engine)