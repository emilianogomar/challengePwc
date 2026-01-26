from app.etl.bronze import ingest_csv
from app.etl.silver import run_silver
from app.etl.gold import build_gold

def seed(csv_path: str):
    ingest_csv(csv_path)
    print(f"data/bronze/csv/{csv_path.split('/')[-1]}")
    run_silver(f"data/bronze/csv/{csv_path.split('/')[-1]}")
    build_gold()
    