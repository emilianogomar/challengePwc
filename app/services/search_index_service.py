from sqlmodel import Session, select
from app.data_access.database import engine
from app.data_access.models import DimProduct
from app.data_access.vector_db import client


def index_products():
    with Session(engine) as session:
        products = session.exec(select(DimProduct)).all()

    docs = [
        {
            "product_id": p.product_id,
            "description": p.description or ""
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
