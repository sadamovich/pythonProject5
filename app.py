from fastapi import FastAPI

from src.api.endpoints import router as api_router


app = FastAPI()
app.include_router(router=api_router)
