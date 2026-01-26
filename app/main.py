from app.data_access.database import init_db
from app.services.etl_service import seed

init_db()
seed("archive/online_retail_II.csv")
