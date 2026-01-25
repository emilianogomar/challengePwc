from pydantic import BaseModel
from typing import Any

class RawRecord(BaseModel):
    id: str
    payload: Any