from fastapi import FastAPI, Request
from test_model import UserCreate, User
import uvicorn
from sqlalchemy.orm import sessionmaker, Session

app = FastAPI()

@app.post("/signup")
async def signup(user: UserCreate, db: Session):
    """
    React로부터 회원가입 데이터를 받는 API.
    """

    db_user = User(firstName=user.firstName, lastName=user.lastName, email=user.email, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return {"message": "회원가입 성공"}

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=3000)
