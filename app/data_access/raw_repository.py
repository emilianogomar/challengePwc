from pathlib import Path
import json
from app.domain.raw import RawJSON, RawCSV

BASE = Path("data/bronze")
JSON_PATH = BASE / "json"
CSV_PATH = BASE / "csv"

JSON_PATH.mkdir(parents=True, exist_ok=True)
CSV_PATH.mkdir(parents=True, exist_ok=True)

def create_json(raw: RawJSON) -> None:
    path = JSON_PATH / f"{raw.id}.json"
    with open(path, "w", encoding="utf-8") as f:
        json.dump(raw.payload, f, ensure_ascii=False, indent=2)

def create_csv(raw: RawCSV) -> None:
    path = CSV_PATH / f"{raw.id}.csv"
    with open(path, "w", encoding="utf-8") as f:
        f.write(raw.content)

def read_json(raw_id: str) -> dict:
    path = JSON_PATH / f"{raw_id}.json"
    if not path.exists():
        raise FileNotFoundError
    with open(path, encoding="utf-8") as f:
        return json.load(f)

def read_csv(raw_id: str) -> str:
    path = CSV_PATH / f"{raw_id}.csv"
    if not path.exists():
        raise FileNotFoundError
    return path.read_text(encoding="utf-8")

def update_json(raw_id: str, payload: dict) -> None:
    path = JSON_PATH / f"{raw_id}.json"
    if not path.exists():
        raise FileNotFoundError
    with open(path, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)

def update_csv(raw_id: str, content: str) -> None:
    path = CSV_PATH / f"{raw_id}.csv"
    if not path.exists():
        raise FileNotFoundError
    path.write_text(content, encoding="utf-8")

def delete_json(raw_id: str) -> None:
    path = JSON_PATH / f"{raw_id}.json"
    if not path.exists():
        raise FileNotFoundError
    path.unlink()

def delete_csv(raw_id: str) -> None:
    path = CSV_PATH / f"{raw_id}.csv"
    if not path.exists():
        raise FileNotFoundError
    path.unlink()
