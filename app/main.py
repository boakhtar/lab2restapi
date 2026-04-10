from fastapi import FastAPI
from app.controllers import item_controller
from app.database.session import engine, Base


Base.metadata.create_all(bind=engine)

app = FastAPI(title="REST API Lab 2", version="1.0.0")

app.include_router(item_controller.router)

@app.get("/")
def root():
    return {"message": "REST API is running", "endpoints": ["/items"]}