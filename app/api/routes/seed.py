from fastapi import APIRouter
from app.services.etl_service import seed

router = APIRouter(prefix="/seed")

@router.post("")
def seed_data():
    seed("archive/online_retail_II.csv")
    return {"status":"ok"}
