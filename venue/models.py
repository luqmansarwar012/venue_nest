from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from sqlalchemy.orm import relationship
from database.service import Base
from core.enums import VenueStatus


class Venue(Base):
    __tablename__ = "venues"

    id = Column(Integer, primary_key=True, autoincrement=True)

    name = Column(String, nullable=False)

    location = Column(String, nullable=False)

    status = Column(Enum(VenueStatus), default=VenueStatus.ACTIVE, nullable=False)

    owner_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    owner = relationship("User", back_populates="venues")

    bookings = relationship("Booking", back_populates="venue")
