from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.farmer import Farmer
from app.schemas.farmer import FarmerCreate, FarmerResponse

router = APIRouter()

@router.post("/", response_model=FarmerResponse)
def create_farmer(
    farmer_data: FarmerCreate,
    db: Session = Depends(get_db)
):

    new_farmer = Farmer(
        name=farmer_data.name,
        phone_no=farmer_data.phone_no,
        address=farmer_data.address
    )

    db.add(new_farmer)
    db.commit()
    db.refresh(new_farmer)

    return new_farmer