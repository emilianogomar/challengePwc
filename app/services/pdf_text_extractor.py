from pypdf import PdfReader
from pathlib import Path

def extract_text(pdf_path: Path) -> str:
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text
