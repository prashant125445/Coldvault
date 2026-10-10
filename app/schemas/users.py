from pydantic import BaseModel, Field, EmailStr


class UserCreate(BaseModel):

    name: str = Field(
        min_length=2,
        max_length=100
    )

    email: EmailStr
    name_of_cold_storage: str = Field(
        min_length=2,
        max_length=100
    )

    password: str = Field(
        min_length=6
    )
    
    

class UserLogin(BaseModel):
    email: EmailStr
    password: str
    


class UserResponse(BaseModel):

    id: int
    name: str
    email: EmailStr
    is_active: bool
    name_of_cold_storage: str
    class Config:
        from_attributes = True