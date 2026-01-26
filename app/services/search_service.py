from app.data_access.vector_db import client

def search(q: str):
    return client().collections["products"].documents.search({
        "q":q,
        "query_by":"description"
    })