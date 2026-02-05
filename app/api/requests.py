from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.schemas.requests import RequestCreate, RequestResponse
from app.db.crud.requests import create_request, get_requests

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=RequestResponse)
def create(data: RequestCreate, db: Session = Depends(get_db)):
    return create_request(db, data)

@router.get("/", response_model=list[RequestResponse])
def list_requests(db: Session = Depends(get_db)):
    return get_requests(db)
