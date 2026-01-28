from sqlmodel import Session, select
from app.data_access.database import engine
from app.data_access.models import DimProduct
from app.data_access.vector_db import client

def reset_collections():

    ts = client()

    for name in ["products", "documents"]:
        try:
            ts.collections[name].delete()
            print(f"Deleted {name}")
        except Exception:
            print(f"{name} does not exist")

def index_products():
    with Session(engine) as session:
        products = session.exec(select(DimProduct)).all()

    docs = [
        {
            "product_id": p.product_id,
            "description": p.description or "",
            "source": "product"
        }
        for p in products
    ]

    if not docs:
        return {"indexed": 0}

    client().collections["products"].documents.import_(
        docs,
        {"action": "upsert"}
    )

    return {"indexed": len(docs)}
