from app.etl.bronze import ingest_csv
from app.etl.silver import run_silver

def seed(csv_path: str):
    ingest_csv(csv_path)
    print(f"data/bronze/csv/{csv_path.split('/')[-1]}")
    run_silver(f"data/bronze/csv/{csv_path.split('/')[-1]}")
    