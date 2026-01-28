from fastapi import UploadFile
from app.data_access.pdf_repository import save_pdf
from app.services.pdf_text_extractor import extract_text
from app.services.pdf_index_service import index_pdf

def ingest_pdf(raw_id: str, file: UploadFile):
    pdf_path = save_pdf(raw_id, file)
    text = extract_text(pdf_path)
    index_pdf(raw_id, text)
