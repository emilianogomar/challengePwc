from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from app.services.raw_pdf_service import ingest_pdf
from app.data_access.pdf_repository import delete_pdf
from app.api.deps import get_current_user

router = APIRouter(prefix="/raw/pdf", tags=["raw-pdf"])

@router.post("")
def upload_pdf(
    raw_id: str,
    file: UploadFile = File(...),
    user: str = Depends(get_current_user)
):
    ingest_pdf(raw_id, file)
    return {"status": "uploaded", "id": raw_id}


@router.delete("/{raw_id}")
def delete_pdf_route(
    raw_id: str,
    user: str = Depends(get_current_user)
):
    try:
        delete_pdf(raw_id)
        return {"status": "deleted"}
    except FileNotFoundError:
        raise HTTPException(404, "PDF not found")
