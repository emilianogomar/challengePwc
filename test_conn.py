from sqlmodel import Session, select
from sqlalchemy import text
from app.data_access.database import engine
from app.data_access.models import DimProduct,DimCustomer,DimCountry,FactSales

# with Session(engine) as session:
#     statement = select(DimCountry)
#     results = session.exec(statement).all()

#     for row in results:
#         print(row)


with Session(engine) as session:
    result = session.exec(
        text("SELECT * FROM gold_sales_by_country")
    )

    for row in result:
        print(row.country_name, row.quantity, row.total_amount)
