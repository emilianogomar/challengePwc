from sqlmodel import SQLModel, create_engine
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
print("DB FILE LOADED FROM:", BASE_DIR)

DB_PATH = BASE_DIR / "data" / "silver" / "warehouse.db"

print("DB WILL BE CREATED AT:", DB_PATH)

DB_PATH.parent.mkdir(parents=True,exist_ok=True)

DATABASE_URL = f"sqlite:///{DB_PATH}"

engine = create_engine(DATABASE_URL,echo=False)

def init_db() -> None:
    SQLModel.metadata.create_all(engine)