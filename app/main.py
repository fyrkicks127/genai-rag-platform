from fastapi import FastAPI
from app.api.health import router as health_router
from app.api.requests import router as requests_router
from app.api.approvals import router as approvals_router

app = FastAPI(title="GenAI RAG Platform")

app.include_router(health_router, prefix="/api/v1/health")
app.include_router(requests_router, prefix="/api/v1/requests")
app.include_router(approvals_router, prefix="/api/v1/approvals")

@app.get("/")
def root():
    return {"message": "GenAI RAG Platform is running"}
