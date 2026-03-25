from fastapi import FastAPI

from app.routes.health import router as health_router
from app.routes.jobs import router as jobs_router
from app.routes.webhooks import router as webhooks_router

app = FastAPI(title="ERPNext Integration Hub")

app.include_router(health_router)
app.include_router(webhooks_router)
app.include_router(jobs_router)
