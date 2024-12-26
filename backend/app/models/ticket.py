from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db.base import Base

class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True, autoincrement=True)
    departure = Column(String(50), nullable=False)
    departure_airport = Column(String(100), nullable=False)
    departure_airport_code = Column(String(10), nullable=False)
    destination = Column(String(50), nullable=False)
    destination_airport = Column(String(100), nullable=False)
    destination_airport_code = Column(String(10), nullable=False)
    departure_date = Column(String(20), nullable=False)
    destination_date = Column(String(20), nullable=False)
    departure_time = Column(String(10), nullable=False)
    destination_time = Column(String(10), nullable=False)
    duration = Column(String(20), nullable=False)
    airline = Column(String(50), nullable=False)
    flightClass = Column(String(20), nullable=False)
    price = Column(Integer, nullable=False) 