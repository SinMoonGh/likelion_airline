from pydantic import BaseModel

class UserCreate(BaseModel):
    firstName: str
    lastName: str
    email: str
    password: str 

class UserLogin(BaseModel):
    email: str
    password: str

