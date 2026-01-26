from sqlmodel import Session, select
from app.data_access.database import engine
from app.data_access.models import DimProduct

with Session(engine) as session:
    statement = select(DimProduct)
    results = session.exec(statement).all()

    for row in results:
        print(row)
