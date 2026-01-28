from fastapi import APIRouter
from app.services.etl_service import seed
from app.services.search_index_service import index_products, reset_collections
from app.data_access.vector_db import create_products_collection
from app.services.pdf_index_service import ensure_collection

router = APIRouter(prefix="/seed", tags=["seed"])

@router.post("")
def seed_data():
    seed("archive/online_retail_II.csv")
    reset_collections()
    create_products_collection()
    ensure_collection()
    index_products()
    return {"status":"ok"}
