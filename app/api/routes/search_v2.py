from fastapi import APIRouter, Query
from app.services.search_service import search

router = APIRouter(
    prefix="/search",
    tags=["search-v2"]
)

@router.get("/")
def search_v2(
    q: str = Query(..., min_length=2),
    source: str = Query("all", enum=["all", "product", "pdf"])
):
    result = search(q=q, source=source)

    result["version"] = "v2"
    return result
