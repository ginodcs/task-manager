from app.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)

    # Relación con Client
    client_id = Column(Integer, ForeignKey("clients.id"), nullable=False)
    client = relationship("Client", back_populates="projects")
    
    name = Column(String, index=True)
    iconUrl = Column(String, unique=True, index=True)
    color = Column(String, unique=True, index=True)

    # Relación con Project
    tasks = relationship("Task", back_populates="project", cascade="all, delete")