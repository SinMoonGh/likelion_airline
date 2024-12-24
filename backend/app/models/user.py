from sqlalchemy import Column, Integer, String
from db.base import Base

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, autoincrement=True)
    firstName = Column(String(5), nullable=False)
    lastName = Column(String(5), nullable=False)
    email = Column(String(30), unique=True, nullable=False)
    password = Column(String(30), nullable=False) 