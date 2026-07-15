from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.api.health import router as health_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting Nexus AI Workspace")
    yield
    print("Shutting Down Nexus AI Workspace")

app = FastAPI(
    title="Nexus AI Workspace",
    version="0.1.0",
    lifespan = lifespan,
)

app.include_router(health_router)