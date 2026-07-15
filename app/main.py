from contextlib import asynccontextmanager
from fastapi import FastAPI

from app.api.health import router as health_router
from app.core.config import settings

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting Nexus AI Workspace")
    yield
    print("Shutting Down Nexus AI Workspace")

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    lifespan = lifespan,
)

app.include_router(health_router)