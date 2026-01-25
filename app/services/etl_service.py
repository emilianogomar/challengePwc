from app.etl.bronze import ingest_csv

def seed(csv_path: str):
    ingest_csv(csv_path)