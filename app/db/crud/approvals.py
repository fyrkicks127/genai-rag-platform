from sqlalchemy.orm import Session
from app.db.models import Approval, BudgetRequest, RequestStatus

def approve_request(db: Session, data):
    request = db.query(BudgetRequest).filter(BudgetRequest.id == data.request_id).first()

    if not request:
        raise ValueError("Request not found")

    request.status = RequestStatus(data.status)

    approval = Approval(
        request_id=data.request_id,
        approved_by_id=data.approved_by_id,
        status=data.status,
        comment=data.comment
    )

    db.add(approval)
    db.commit()
    db.refresh(approval)
    return approval
