from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.schemas.approvals import ApprovalCreate
from app.db.crud.approvals import approve_request

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def approve(data: ApprovalCreate, db: Session = Depends(get_db)):
    try:
        return approve_request(db, data)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))