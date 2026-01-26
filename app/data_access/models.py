from sqlmodel import SQLModel, Field
from datetime import date

class DimProduct(SQLModel, table=True):
    product_id: str = Field(primary_key=True)
    description: str

class DimCustomer(SQLModel, table=True):
    customer_id: str = Field(primary_key=True)
    country_id: str

class DimCountry(SQLModel, table=True):
    country_id: str = Field(primary_key=True)
    country_name: str

class DimDate(SQLModel, table=True):
    date_id: date = Field(primary_key=True)
    day: int
    month: int
    year: int

class DimChannel(SQLModel, table=True):
    channel_id: str = Field(primary_key=True)
    channel_name: str

class FactSales(SQLModel, table=True):
    order_id: str = Field(primary_key=True)
    product_id: str
    customer_id: str
    date_id: date
    channel_id: str
    quantity: int
    price: float
    total_amount: float