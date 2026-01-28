import pandas as pd
from app.data_access.database import engine

def build_gold():
    fact = pd.read_sql_table("factsales",engine)
    customer = pd.read_sql_table("dimcustomer",engine)
    country = pd.read_sql_table("dimcountry",engine)
    product = pd.read_sql_table("dimproduct", engine)

    df = (
        fact
        .merge(customer, on="customer_id")
        .merge(country, on="country_id")
        .groupby("country_name", as_index=False)
        .agg(
            quantity=("quantity","sum"),
            total_amount=("total_amount","sum")
        )
    )

    df.to_sql(
        "gold_sales_by_country",
        engine,
        if_exists="replace",
        index=False
    )

    df2 = (
        fact
        .merge(product, on="product_id")
        .groupby(
            ["product_id", "description"],
            as_index=False
        )
        .agg(
            total_quantity=("quantity", "sum"),
            total_revenue=("total_amount", "sum"),
            orders=("order_id", "nunique")
        )
    )

    df2.to_sql(
        "gold_sales_by_product",
        engine,
        if_exists="replace",
        index=False
    )

    df3 = (
        fact
        .merge(customer, on="customer_id")
        .groupby(
            ["customer_id", "country_id"],
            as_index=False
        )
        .agg(
            lifetime_value=("total_amount", "sum"),
            total_orders=("order_id", "nunique"),
            total_items=("quantity", "sum"),
            avg_order_value=("total_amount", "mean")
        )
    )

    df3.to_sql(
        "gold_customer_lifetime_value",
        engine,
        if_exists="replace",
        index=False
    )

    # df = pd.read_sql("""
    #     SELECT dco.country_name, 
    #            SUM(fs.quantity) as quantity,
    #            SUM(fs.total_amount) as total_amount
    #     FROM factsales fs
    #     JOIN dimcustomer dc ON fs.customer_id = dc.customer_id
    #     JOIN dimcountry dco ON dc.country_id = dco.country_id
    #     GROUP BY dco.country_name
    # """,engine)

    # df.to_sql("gold_sales_by_country", engine, if_exists="replace", index=False)