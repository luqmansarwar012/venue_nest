import enum


class UserRole(str, enum.Enum):
    SUPERADMIN = "superadmin"
    VENUE_OWNER = "venue_owner"
    CUSTOMER = "customer"


class VenueStatus(str, enum.Enum):
    BOOKED = "booked"
    AVAILABLE = "available"
    UNDER_MAINTENANCE = "under_maintenance"
    INACTIVE = "inactive"


class BookingStatus(str, enum.Enum):
    PENDING = "pending"
    CONFIRMED = "confirmed"
    CANCELLED = "cancelled"
