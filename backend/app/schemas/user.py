from pydantic import BaseModel

class UserCreate(BaseModel):
    firstName: str
    lastName: str
    email: str
    password: str 

class UserLogin(BaseModel):
    email: str
    password: str

class ChangePasswordRequest(BaseModel):
    userId: int
    oldPassword: str
    newPassword: str