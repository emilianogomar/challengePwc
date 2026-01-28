from fastapi import APIRouter, Query
from app.data_access.vector_db import client

router = APIRouter(
    prefix="/search",
    tags=["search-v1"]
)

@router.get("/")
def search_v1(
    q: str = Query(..., min_length=1)
):
    c = client()

    products = c.collections["products"].documents.search({
        "q": q,
        "query_by": "description",
        "filter_by": "source:=product"
    })

    return {
        "version": "v1",
        "query": q,
        "results": {
            "products": products
        }
    }
