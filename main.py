from logger_config import logger
from fastapi import FastAPI
import database

app = FastAPI()


@app.get("/")
def root():
    logger.info("Received request to root endpoint")
    return {"message": "Hello World"}
