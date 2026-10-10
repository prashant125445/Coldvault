from pydantic import BaseModel, Field


class CreateBooking(BaseModel):

    farmer_name: str = Field(min_length=1)

    farmer_phone_no: str = Field(
        min_length=10,
        max_length=11
    )

    farmer_address: str = Field(min_length=5)

    slots: int = Field(gt=0)

    duration_days: int = Field(gt=0)


    start_date: str = Field(min_length=1)

    end_date: str = Field(min_length=1)


class BookingResponse(BaseModel):

    id: int

    farmer_name: str
    farmer_phone_no: str
    farmer_address: str

    chamber_id: int

    slots: int
    duration_days: int

    total_rent: float

    # booking_date: str
    start_date: str
    end_date: str

    class Config:
        from_attributes = True