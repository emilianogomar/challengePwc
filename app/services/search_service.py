from app.data_access.vector_db import client


def search(q: str):
    c = client()

    products_res = c.collections["products"].documents.search({
        "q": q,
        "query_by": "description"
    })

    docs_res = c.collections["documents"].documents.search({
        "q": q,
        "query_by": "text",
        "filter_by": "source:pdf"
    })

    return {
        "query": q,
        "products": products_res["hits"],
        "documents": docs_res["hits"]
    }
