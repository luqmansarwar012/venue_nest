from core.service import logger
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    logger.info("Received request to root endpoint")
    return {"message": "Hello World"}
