from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.session import get_db
from models.ticket import Ticket, PurchaseTicket
from schemas.ticket import TicketCreate, PurchaseRequest
from datetime import datetime
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


@router.post("/purchase/{flightId}")
async def purchase_ticket(request: PurchaseRequest, db: Session = Depends(get_db)):
    # existing_ticket(request.flightId, request.userId, db)
    
    new_ticket = PurchaseTicket(
        flightId=request.flightId,
        userId=request.userId,
        purchase_date=datetime.now().strftime("%Y-%m-%d"),
        purchase_time=datetime.now().strftime("%H:%M:%S")
    )
    db.add(new_ticket)
    db.commit()
    db.refresh(new_ticket)
    return {"message": "구매 완료", "ticket": new_ticket.id}

def existing_ticket(flightId: int, userId: int, db: Session = Depends(get_db)):
    existing_ticket = db.query(PurchaseTicket).filter_by(userId=userId, flightId=flightId).first()
    if existing_ticket:
        raise HTTPException(status_code=400, detail="이미 해당 티켓을 구매하셨습니다.")


@router.get("/user")
async def get_user_tickets(db: Session = Depends(get_db)):
    user_tickets = db.query(PurchaseTicket).filter_by(userId=userId).all()
    return user_tickets