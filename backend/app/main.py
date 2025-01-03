import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.v1.user.router import router as user_router
from api.v1.ticket.router import router as ticket_router
from api.v1.flights.router import router as flights_router
from db.base import Base
from db.session import engine

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_router, prefix="/api/v1/user", tags=["user"])
app.include_router(ticket_router, prefix="/api/v1/tickets", tags=["tickets"])
app.include_router(flights_router, prefix="/api/v1/flights", tags=["flights"])

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000) 