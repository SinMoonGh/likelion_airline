from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.session import get_db
from models.ticket import Ticket
from schemas.ticket import TicketCreate

router = APIRouter()

@router.post("/create")
async def create_ticket(ticket: TicketCreate, db: Session = Depends(get_db)):
    db_ticket = Ticket(
        departure=ticket.departure,
        departure_airport=ticket.departure_airport,
        departure_airport_code=ticket.departure_airport_code,
        destination=ticket.destination,
        destination_airport=ticket.destination_airport,
        destination_airport_code=ticket.destination_airport_code,
        departure_date=ticket.departure_date,
        destination_date=ticket.destination_date,
        departure_time=ticket.departure_time,
        destination_time=ticket.destination_time,
        duration=ticket.duration,
        airline=ticket.airline,
        flightClass=ticket.flightClass,
        price=ticket.price
    )
    
    db.add(db_ticket)
    db.commit()
    db.refresh(db_ticket)
    
    return {"message": "티켓 생성 완료", "ticket_id": db_ticket.id} 

