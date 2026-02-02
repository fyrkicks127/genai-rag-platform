from fastapi import FastAPI
from app.api.health import router as health_router

app = FastAPI(title="GenAI RAG Platform")

app.include_router(health_router, prefix="/api/v1/health")

@app.get("/")
def root():
    return {"message": "GenAI RAG Platform is running"}
