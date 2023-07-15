from fastapi import FastAPI
from app.api import router

api_app = FastAPI()

api_app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(api_app, host="0.0.0.0", port=8000)
