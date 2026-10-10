from sqlalchemy import Column, Integer, String
from app.core.database import Base


class Farmer(Base):
    __tablename__ = "farmers"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)

    phone_no = Column(
        String(11),
        nullable=False,
        unique=True
    )

    address = Column(String, nullable=False)
    
    bill = Column(Integer, default=0)  # Added bill column to track the farmer's bill