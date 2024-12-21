# main.py
import uvicorn
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import Database
from models import UserCreate, User
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],  # React 앱 주소
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

database = Database()

# 회원가입 엔드포인트
@app.post("/signup")
async def sign_up(user: UserCreate, db: Session = Depends(database.get_db)):
    db_user = User(
        firstName=user.firstName,
        lastName=user.lastName,
        email=user.email,
        password=user.password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    
    return {"message": "회원가입 성공"}

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
