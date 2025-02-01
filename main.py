import uvicorn
from fastapi import FastAPI

from controller.healthcheck import router as healthcheck_router

app = FastAPI()
app.include_router(healthcheck_router)

