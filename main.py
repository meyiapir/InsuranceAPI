import uvicorn
from fastapi import FastAPI
from tortoise import run_async

from app.api import router
from app.database import init_db
from app.tariff_loader import load_tariff_to_db
from loguru import logger

api_app = FastAPI()

api_app.include_router(router)

if __name__ == "__main__":
    try:
        logger.info("Starting server...")
        run_async(init_db())
        run_async(load_tariff_to_db('app/tariff.json'))
        uvicorn.run(api_app, host="0.0.0.0", port=8000)
    except Exception as e:
        logger.error(f"Error starting server: {e}")
