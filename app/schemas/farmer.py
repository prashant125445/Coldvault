from pydantic import BaseModel, Field


class FarmerCreate(BaseModel):

    name: str = Field(min_length=1)

    phone_no: str = Field(
        min_length=10,
        max_length=11
    )

    address: str = Field(min_length=5)


class FarmerResponse(BaseModel):

    id: int
    name: str
    phone_no: str
    address: str

    class Config:
        from_attributes = True