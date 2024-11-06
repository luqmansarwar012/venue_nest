from sqlalchemy import Column, Integer, DateTime, ForeignKey, Enum, Numeric, Boolean
from sqlalchemy.orm import relationship
from core.enums import BookingStatus
from database.service import Base


class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, autoincrement=True)

    booking_time = Column(DateTime, nullable=False)

    venue_id = Column(Integer, ForeignKey("venues.id"), nullable=False)
    venue = relationship("Venue", back_populates="bookings")

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    user = relationship("User", back_populates="bookings")

    bill = Column(Numeric(10, 2), nullable=False, default=0.00)

    paid = Column(Boolean, nullable=False, default=False)

    status = Column(Enum(BookingStatus), default=BookingStatus.PENDING)
