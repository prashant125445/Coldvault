from pydantic import BaseModel, Field


class ChamberCreate(BaseModel):
    name: str = Field(min_length=1)
    total_slots: int = Field(gt=0)
    rent_per_slot: float = Field(gt=0)


class ChamberResponse(BaseModel):
    id: int
    name: str
    total_slots: int
    occupied_slots: int
    available_slots: int
    rent_per_slot: float

    class Config:
        from_attributes = True