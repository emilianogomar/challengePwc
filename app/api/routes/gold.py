from fastapi import APIRouter
from app.data_access.database import engine
import pandas as pd

router = APIRouter(prefix="/gold", tags=["gold"])

@router.get("/sales-by-country")
def sales_by_country():
    df = pd.read_sql_table("gold_sales_by_country", engine)
    return df.to_dict(orient="records")

@router.get("/sales-by-product")
def sales_by_product():
    df = pd.read_sql_table("gold_sales_by_product", engine)
    return df.to_dict(orient="records")

@router.get("/customer-lifetime-value")
def customer_lifetime_value():
    df = pd.read_sql_table("gold_customer_lifetime_value", engine)
    return df.to_dict(orient="records")
