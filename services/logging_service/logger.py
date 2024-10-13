import logging
from fastapi import FastAPI

app = FastAPI()
logger = logging.getLogger("security_tool")

@app.post("/log")
def log_message(level: str, message: str):
    """Log messages with levels like INFO, WARN, ERROR."""
    if level == "info":
        logger.info(message)
    elif level == "warn":
        logger.warning(message)
    elif level == "error":
        logger.error(message)
    return {"status": "logged"}
