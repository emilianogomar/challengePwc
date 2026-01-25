from pydantic import BaseModel
from datetime import date

class Sales(BaseModel):
    order_id: str
    product_id: str
    customer_id: str
    date: date
    quantity: int
    unit_price: float
    total_amount: float