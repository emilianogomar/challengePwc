from app.data_access.vector_db import client

COLLECTION = "documents"

def ensure_collection():
    ts = client()
    if COLLECTION not in [c["name"] for c in ts.collections.retrieve()]:
        ts.collections.create({
            "name": COLLECTION,
            "fields": [
                {"name": "id", "type": "string"},
                {"name": "text", "type": "string"},
                {"name": "source", "type": "string"}
            ]
        })

def index_pdf(pdf_id: str, text: str):
    ensure_collection()
    ts = client()
    ts.collections[COLLECTION].documents.upsert({
        "id": pdf_id,
        "text": text,
        "source": "pdf"
    })
