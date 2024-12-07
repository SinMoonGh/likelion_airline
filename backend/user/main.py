# main.py
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, User
from models import UserCreate
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],  # React 앱 주소
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 의존성 주입을 통해 데이터베이스 세션을 얻는 함수
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 회원가입 엔드포인트
@app.post("/signup")
async def sign_up(user: UserCreate, db: Session = Depends(get_db)):
    # User 객체 생성 및 데이터베이스에 추가
    db_user = User(firstName=user.firstName, lastName=user.lastName, email=user.email, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    
    return {"message": "회원가입 성공"}
