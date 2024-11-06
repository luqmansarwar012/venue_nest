from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import relationship
from database.service import Base
from core.enums import UserRole
from typing import List


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    role = Column(Enum(UserRole), nullable=False, default=UserRole.CUSTOMER)

    bookings = relationship("Booking", back_populates="customer")
    venues = relationship("Venue", back_populates="owner")
