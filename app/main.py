from fastapi import FastAPI
from app.core.database import engine , Base
from app.routers.chamber import router as chamber_router
from app.routers.booking import router as booking_router
from app.routers.auth import router as user_router
Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(chamber_router)
app.include_router(booking_router)

app.include_router(user_router)
@app.get("/")
def home():
    return {
        "message": "ColdVault API is running"
    }