# models.py
from pydantic import BaseModel
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

# SQLAlchemy의 declarative_base를 사용하여 데이터베이스 모델의 베이스 클래스를 생성합니다.
Base = declarative_base()

class User(Base):
    __tablename__ = "user"

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

