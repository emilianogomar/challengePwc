from fastapi import APIRouter, Depends, HTTPException
from app.domain.raw import RawJSON, RawCSV
from app.services import raw_service
from app.api.deps import get_current_user

router = APIRouter(prefix="/raw", tags=["raw"])

# JSON Endpoints

@router.post("/json")
def create_json(raw: RawJSON, user=Depends(get_current_user)):
    raw_service.create_raw_json(raw)
    return {"status": "created", "id": raw.id}

@router.get("/json/{raw_id}")
def get_json(raw_id: str, user=Depends(get_current_user)):
    try:
        return raw_service.read_raw_json(raw_id)
    except FileNotFoundError:
        raise HTTPException(404, "JSON not found")

@router.put("/json/{raw_id}")
def update_json(raw_id: str, payload: dict, user=Depends(get_current_user)):
    try:
        raw_service.update_raw_json(raw_id, payload)
        return {"status": "updated"}
    except FileNotFoundError:
        raise HTTPException(404, "JSON not found")

@router.delete("/json/{raw_id}")
def delete_json(raw_id: str, user=Depends(get_current_user)):
    try:
        raw_service.delete_raw_json(raw_id)
        return {"status": "deleted"}
    except FileNotFoundError:
        raise HTTPException(404, "JSON not found")

# CSV Endpoints

@router.post("/csv")
def create_csv(raw: RawCSV, user=Depends(get_current_user)):
    raw_service.create_raw_csv(raw)
    return {"status": "created", "id": raw.id}

@router.get("/csv/{raw_id}")
def get_csv(raw_id: str, user=Depends(get_current_user)):
    try:
        return raw_service.read_raw_csv(raw_id)
    except FileNotFoundError:
        raise HTTPException(404, "CSV not found")

@router.put("/csv/{raw_id}")
def update_csv(raw_id: str, content: str, user=Depends(get_current_user)):
    try:
        raw_service.update_raw_csv(raw_id, content)
        return {"status": "updated"}
    except FileNotFoundError:
        raise HTTPException(404, "CSV not found")

@router.delete("/csv/{raw_id}")
def delete_csv(raw_id: str, user=Depends(get_current_user)):
    try:
        raw_service.delete_raw_csv(raw_id)
        return {"status": "deleted"}
    except FileNotFoundError:
        raise HTTPException(404, "CSV not found")
