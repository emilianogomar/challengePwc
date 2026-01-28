from pathlib import Path
from fastapi import UploadFile

BASE_PATH = Path("data/bronze/pdf")
BASE_PATH.mkdir(parents=True, exist_ok=True)

def save_pdf(raw_id: str, file: UploadFile) -> Path:
    path = BASE_PATH / f"{raw_id}.pdf"
    with open(path, "wb") as f:
        f.write(file.file.read())
    return path

def delete_pdf(raw_id: str) -> None:
    path = BASE_PATH / f"{raw_id}.pdf"
    if not path.exists():
        raise FileNotFoundError
    path.unlink()

def get_pdf_path(raw_id: str) -> Path:
    path = BASE_PATH / f"{raw_id}.pdf"
    if not path.exists():
        raise FileNotFoundError
    return path
