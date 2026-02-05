from pydantic import BaseModel
from enum import Enum
from datetime import datetime

class RequestStatus(str, Enum):
    PENDING = "PENDING"
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"

class RequestCreate(BaseModel):
    title: str
    description: str
    created_by_id: int

class RequestResponse(BaseModel):
    id: int
    title: str
    description: str
    status: RequestStatus
    created_at: datetime

    class Config:
        from_attributes = True
