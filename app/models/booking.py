from sqlalchemy import Column, Integer, String, Float, ForeignKey
from app.core.database import Base


class Booking(Base):

    __tablename__ = "bookings"
      
    farmer_id = Column(
     Integer,
     ForeignKey("farmers.id"),
     nullable=False
) 
    id = Column(Integer, primary_key=True, index=True)

    # farmer_phone_no = Column(String(11), nullable=False)
    # farmer_name = Column(String, nullable=False)
    # farmer_address = Column(String, nullable=False)

    chamber_id = Column(
        Integer,
        ForeignKey("chambers.id"),
        nullable=False
    )

    slots = Column(Integer, nullable=False)

    duration_days = Column(Integer, nullable=False)

    rent_per_slot = Column(Float, nullable=False)
    total_rent = Column(Float, nullable=False)

    # booking_date = Column(String, nullable=False)
    start_date = Column(String, nullable=False)
    end_date = Column(String, nullable=False)