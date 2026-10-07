from fastapi import FastAPI
from app.db.database import engine
from app.db.session import Base
from app.routes import apirouter


Base.metadata.create_all(engine)

app=FastAPI()

app.include_router(apirouter)
