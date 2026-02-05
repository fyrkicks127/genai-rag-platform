from sqlalchemy.orm import Session
from app.db.models import BudgetRequest, RequestStatus

def create_request(db: Session, data):
    req = BudgetRequest(
        title=data.title,
        description=data.description,
        created_by_id=data.created_by_id,
        status=RequestStatus.PENDING
    )
    db.add(req)
    db.commit()
    db.refresh(req)
    return req

def get_requests(db: Session):
    return db.query(BudgetRequest).all()
