import pandas as pd
from sqlmodel import Session
from app.data_access.database import engine
from app.data_access.models import DimProduct,DimCustomer,DimCountry,DimChannel,DimDate, FactSales

COUNTRY_MAP = {
    "United Kingdom": "UK",
    "France": "FR",
    "Germany": "DE",
    "Spain": "ES"
}

def run_silver(csv_path: str):
    df = pd.read_csv(csv_path)

    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"]).dt.date
    df["total_amount"] = df["Quantity"] * df["Price"]

    with Session(engine) as session:
        for _, r in df.iterrows():
            # COUNTRY
            country_id = COUNTRY_MAP.get(str(r["Country"]), "OTHER")
            session.merge(DimCountry(
            country_id=country_id,
            country_name=str(r["Country"])
            ))
            # PRODUCT
            session.merge(DimProduct(
                product_id=str(r["StockCode"]),
                description=str(r["Description"])
            ))
            # CUSTOMER
            session.merge(DimCustomer(
                customer_id=str(r["CustomerID"]),
                country_id=country_id
            ))
            # DATE
            d = r["InvoiceDate"]
            session.merge(DimDate(
                date_id=d,
                day=d.day,
                month=d.month,
                year=d.year
            ))
            # CHANNEL (hardcoded)
            session.merge(DimChannel(
                channel_id="online",
                channel_name="Online Store"
            ))
            # SALES
            session.merge(FactSales(
                order_id=str(r["Invoice"]),
                product_id=str(r["StockCode"]),
                customer_id=str(r["CustomerID"]),
                date_id=d,
                channel_id="online",
                quantity=int(r["Quantity"]),
                price=float(r["Price"]),
                total_amount=float(r["total_amount"])
            ))
        session.commit()
