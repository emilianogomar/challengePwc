from pydantic import BaseModel

class Customer(BaseModel):
    costumer_id: str
    country: str