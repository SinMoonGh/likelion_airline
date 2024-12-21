from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    firstName = Column(String(5), nullable=False)
    lastName = Column(String(5), nullable=False)
    email = Column(String(30), unique=True, nullable=False)
    password = Column(String(30), nullable=False)


class UserCreate(BaseModel):
    firstName: str
    lastName: str
    email: str
    password : str