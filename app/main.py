from contextlib import asynccontextmanager
from fastapi import FastAPI

from app.api.health import router as health_router
from app.core.config import settings
from app.core.logging import logger

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Starting Nexus AI Workspace...")
    yield
    logger.info("Shutting down Nexus AI Workspace...")

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    lifespan = lifespan,
)

app.include_router(health_router)