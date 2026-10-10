from sqlalchemy import Column, Integer, String, Boolean

from app.core.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)
    
   

    email = Column(String, unique=True, nullable=False, index=True)
    name_of_cold_storage: str = Column(String, nullable=False)
    password = Column(String, nullable=False)

    is_active = Column(Boolean, default=True)