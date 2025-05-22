from datetime import datetime
from pydantic import BaseModel
from app.models.task_model import StatusEnum

class TaskBase(BaseModel):
    title: str
    description: str | None = None

class TaskCreate(TaskBase):
    pass

class TaskRead(TaskBase):
    id: int
    status: StatusEnum
    created_at: datetime
    completed_at: datetime | None = None
    hours_spent: int
    
    class Config:
        orm_mode = True

class TaskUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    status: StatusEnum | None = None
    created_at: datetime | None = None
    completed_at: datetime | None = None
    hours_spent: int | None = None
