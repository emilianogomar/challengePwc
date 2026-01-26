import typesense

def client():
    return typesense.Client({
            "nodes": [{
                "host":"localhost",
                "port":"8108",
                "protocol":"http"
            }],
            "api_key":"xyz",
            "connection_timeout_seconds": 2
        })

def create_products_collection():
    schema = {
        "name": "products",
        "fields": [
            {"name": "product_id", "type": "string"},
            {"name": "description", "type": "string"}
        ]
    }

    c = client()

    try:
        c.collections["products"].retrieve()
    except:
        c.collections.create(schema)
