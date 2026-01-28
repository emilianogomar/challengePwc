from pydantic import BaseModel
from typing import Any, Literal

class RawJSON(BaseModel):
    id: str
    source: Literal["json"]
    payload: Any

class RawCSV(BaseModel):
    id: str
    source: Literal["csv"]
    content: str  # CSV como texto plano

class RawPDF(BaseModel):
    id: str
    filename: str
