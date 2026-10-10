from sqlalchemy import Column, Integer, String, Float
from app.core.database import Base


class Chamber(Base):

    __tablename__ = "chambers"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)

    total_slots = Column(Integer, nullable=False)

    occupied_slots = Column(Integer, default=0)

    available_slots = Column(Integer, nullable=False)

    rent_per_slot = Column(Float, nullable=False)