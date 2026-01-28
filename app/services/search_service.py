from app.data_access.vector_db import client


def search(q: str,source: str):
    c = client()

    results = {}

    if source in ("all", "product"):
        results["products"] = c.collections["products"].documents.search({
            "q": q,
            "query_by": "description",
            "filter_by": "source:=product"
        })


    if source in ("all", "pdf"):
        results["documents"] = c.collections["documents"].documents.search({
            "q": q,
            "query_by": "text",
            "filter_by": "source:=pdf"
        })

    return {
        "query": q,
        "filter": source,
        "results": results
    }
