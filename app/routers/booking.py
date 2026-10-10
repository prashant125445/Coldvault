from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db

from app.models.booking import Booking
from app.models.chamber import Chamber
from app.models.farmer import Farmer
from app.core.security import get_current_user
from app.models.users import User
from app.schemas.booking import BookingResponse, CreateBooking


router = APIRouter(
    prefix="/chambers",
    tags=["Bookings"]
)


@router.post(
    "/{chamber_id}/bookings",
    response_model=BookingResponse
)
def create_booking(
    chamber_id: int,
    booking_data: CreateBooking,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    #  Find chamber
    chamber = db.query(Chamber).filter(
        Chamber.id == chamber_id
    ).first()

    #  Chamber doesn't exist
    if not chamber:
        raise HTTPException(
            status_code=404,
            detail="Chamber not found"
        )
        
    # Find farmer by phone number
    farmer = db.query(Farmer).filter(
        Farmer.phone_no == booking_data.farmer_phone_no
    ).first()    
    
    if farmer:
    # Existing farmer
     farmer_id = farmer.id

    else:
    # New farmer
     farmer = Farmer(
        name=booking_data.farmer_name,
        phone_no=booking_data.farmer_phone_no,
        address=booking_data.farmer_address
    )

    db.add(farmer)
    db.flush()

    farmer_id = farmer.id

    #  Check available slots
    if booking_data.slots > chamber.available_slots:
        raise HTTPException(
            status_code=400,
            detail="Not enough slots available"
        )

    #  Find farmer using phone number
    farmer = db.query(Farmer).filter(
        Farmer.phone_no == booking_data.farmer_phone_no
    ).first()

    #  Existing farmer
    if farmer:

        # Use existing farmer
        farmer_id = farmer.id

    #  New farmer
    else:

        farmer = Farmer(
            name=booking_data.farmer_name,
            phone_no=booking_data.farmer_phone_no,
            address=booking_data.farmer_address
        )

        db.add(farmer)

        # Generate farmer.id before creating booking
        db.flush()

        farmer_id = farmer.id

    #  Calculate total rent
    total_rent = (
        booking_data.slots *
        chamber.rent_per_slot *
        booking_data.duration_days
    )

    #  Create booking
    new_booking = Booking(

        # Farmer relationship
        farmer_id=farmer_id,

        # Chamber relationship
        chamber_id=chamber_id,

        slots=booking_data.slots,
        duration_days=booking_data.duration_days,

        # Rent comes from chamber
        rent_per_slot=chamber.rent_per_slot,
        total_rent=total_rent,

        start_date=booking_data.start_date,
        end_date=booking_data.end_date
    )

    # Update chamber
    chamber.occupied_slots += booking_data.slots

    chamber.available_slots -= booking_data.slots

    #  Save everything
    db.add(new_booking)

    db.commit()

    #  Refresh booking
    db.refresh(new_booking)

    return new_booking