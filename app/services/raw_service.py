from app.domain.raw import RawJSON, RawCSV
from app.data_access import raw_repository as repo

def create_raw_json(raw: RawJSON):
    repo.create_json(raw)

def create_raw_csv(raw: RawCSV):
    repo.create_csv(raw)

def read_raw_json(raw_id: str):
    return repo.read_json(raw_id)

def read_raw_csv(raw_id: str):
    return repo.read_csv(raw_id)

def update_raw_json(raw_id: str, payload: dict):
    repo.update_json(raw_id, payload)

def update_raw_csv(raw_id: str, content: str):
    repo.update_csv(raw_id, content)

def delete_raw_json(raw_id: str):
    repo.delete_json(raw_id)

def delete_raw_csv(raw_id: str):
    repo.delete_csv(raw_id)
