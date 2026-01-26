import pandas as pd
from app.data_access.database import engine

def build_gold():
    df = pd.read_sql("""
        SELECT dco.country_name, 
               SUM(fs.quantity) as quantity,
               SUM(fs.total_amount) as total_amount
        FROM factsales fs
        JOIN dimcustomer dc ON fs.customer_id = dc.customer_id
        JOIN dimcountry dco ON dc.country_id = dco.country_id
        GROUP BY dco.country_name
    """,engine)

    df.to_sql("gold_sales_by_country", engine, if_exists="replace", index=False)