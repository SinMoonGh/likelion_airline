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


PAGE = 1
LIMIT = 10
@router.get("/user/{userId}")
async def get_user_tickets(userId: int, db: Session = Depends(get_db)):
    user_tickets = db.query(PurchaseTicket).filter(PurchaseTicket.userId == userId).all()
    ticket_ids = [ticket.flightId for ticket in user_tickets]
    matching_tickets_query = db.query(Ticket).filter(Ticket.id.in_(ticket_ids))

    # 페이지네이션
    total_items = matching_tickets_query.count()
    total_pages = (total_items + LIMIT - 1) // LIMIT
    matching_tickets = matching_tickets_query.offset((PAGE - 1) * LIMIT).limit(LIMIT).all()
    return {
        "totalItems": total_items,
        "totalPages": total_pages,
        "currentPage": PAGE,
        "tickets": matching_tickets     
    }
