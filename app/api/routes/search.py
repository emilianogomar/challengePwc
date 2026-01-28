from fastapi import APIRouter
from app.services.search_service import search

router = APIRouter(prefix="/search", tags=["search"])

@router.get("")
def search_endpoint(q: str):
    return search(q)