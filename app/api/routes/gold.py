from fastapi import APIRouter
from app.data_access.database import engine
import pandas as pd

router = APIRouter(prefix="/gold")

@router.get("/sales")
def sales():
    return pd.read_sql("SELECT * FROM gold_sales_by_country",engine).to_dict()