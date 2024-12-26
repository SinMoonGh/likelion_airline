from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.session import get_db
from models.ticket import Ticket

router = APIRouter()

@router.get("/flights")
async def get_flights(page: int = 1, limit: int = 6, db: Session = Depends(get_db)):
    offset = (page - 1) * limit
    total_items = db.query(Ticket).count()
    flights = db.query(Ticket).offset(offset).limit(limit).all()
    total_pages = (total_items + limit - 1) // limit

    return {
        "totalItems": total_items,
        "flights": flights,
        "currentPage": page,
        "totalPages": total_pages
    }