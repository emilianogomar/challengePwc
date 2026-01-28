from app.data_access.database import init_db
from app.api.routes import search_v1,search_v2, seed,gold,raw,raw_pdf
from app.api.deps import get_current_user
from fastapi import FastAPI, Depends

app = FastAPI(
    title="Data Engineering Challenge",
    dependencies=[Depends(get_current_user)]
)

init_db()

app.include_router(seed.router)
app.include_router(gold.router)
app.include_router(search_v1.router, prefix="/api/v1")
app.include_router(search_v2.router, prefix="/api/v2")
app.include_router(raw.router)
app.include_router(raw_pdf.router)

