from pydantic import BaseModel
from enum import Enum

class ApprovalAction(str, Enum):
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"

class ApprovalCreate(BaseModel):
    request_id: int
    approved_by_id: int
    status: ApprovalAction
    comment: str | None = None
