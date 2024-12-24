import jwt
import os
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.session import get_db
from models.user import User
from schemas.user import UserCreate, UserLogin
from datetime import datetime, timedelta

router = APIRouter()

# JWT 설정
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")

@router.post("/signup")
async def sign_up(user: UserCreate, db: Session = Depends(get_db)):
    # 이메일 중복 체크
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="이미 존재하는 이메일입니다")
        
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

@router.post("/login")
async def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(
        User.email == user.email,
        User.password == user.password
    ).first()
    
    if not db_user:
        raise HTTPException(
            status_code=401,
            detail="이메일 또는 비밀번호가 일치하지 않습니다"
        )

    # JWT 토큰 생성
    token_data = {
        "sub": db_user.email,
        "exp": datetime.now() + timedelta(minutes=30)
    }
    token = jwt.encode(token_data, SECRET_KEY, algorithm=ALGORITHM)

    return {
        "message": "로그인 성공",
        "token": token,
        "user": db_user.lastName
    }

