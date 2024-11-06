from fastapi import FastAPI
from logger_config import logger

app = FastAPI()


@app.get("/")
def root():
    logger.info("Received request to root endpoint")
    return {"message": "Hello World"}
