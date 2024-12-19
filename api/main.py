from fastapi import FastAPI
from .models import *
from .database import engine
from .routers import router

app = FastAPI()
app.include_router(router)

Base.metadata.create_all(engine)

@app.get("/")
def read_root():
    return {"message": "Connected to the database!"}
