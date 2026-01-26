from app.data_access.database import init_db
from app.api.routes import seed,gold
from fastapi import FastAPI

app = FastAPI()

init_db()

app.include_router(seed.router)
app.include_router(gold.router)

