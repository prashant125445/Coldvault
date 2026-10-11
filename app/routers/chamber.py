from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.security import get_current_user
from app.models.users import User
from app.core.database import get_db
from app.models.chamber import Chamber
from app.schemas.chamber import ChamberCreate, ChamberResponse


router = APIRouter(
    prefix="/chambers",
    tags=["Chambers"]
)

@router.get("/")
def get_chambers(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return db.query(Chamber).all()

@router.post("/", response_model=ChamberResponse)
def create_chamber(
    chamber: ChamberCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    new_chamber = Chamber(
        name=chamber.name,
        total_slots=chamber.total_slots,
        occupied_slots=0,
        available_slots=chamber.total_slots,
        rent_per_slot=chamber.rent_per_slot
    )

    db.add(new_chamber)
    db.commit()
    db.refresh(new_chamber)

    return new_chamber