from sqlalchemy import Column, Integer, String, DateTime, Enum
from app.database import Base
import enum
from datetime import datetime

class StatusEnum(enum.Enum):
    NEW = "New"
    IN_PROGRESS = "In progress"
    COMPLETED = "Completed"
    BLOCKED = "Blocked"

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, nullable=True)
    status = Column(Enum(StatusEnum), default=StatusEnum.NEW, nullable=False)
    created_at = Column(DateTime, default=datetime.now, nullable=False)
    completed_at = Column(DateTime, nullable=True)
    hours_spent = Column(Integer, default=0, nullable=False)
