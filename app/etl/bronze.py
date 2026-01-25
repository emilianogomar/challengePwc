import shutil
from pathlib import Path

def ingest_csv(src: str):
    dst = Path("data/bronze/csv") / Path(src).name
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy(src, dst)