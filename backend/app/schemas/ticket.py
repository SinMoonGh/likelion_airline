from pydantic import BaseModel

class TicketCreate(BaseModel):
    departure: str
    departure_airport: str
    departure_airport_code: str
    destination: str
    destination_airport: str
    destination_airport_code: str
    departure_date: str
    destination_date: str
    departure_time: str
    destination_time: str
    duration: str
    airline: str
    flightClass: str
    price: int

class PurchaseRequest(BaseModel):
    flightId: int
    userId: int