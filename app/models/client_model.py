from app.database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class Client(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    logoUrl = Column(String, unique=True, index=True)

    # Relación con Project
    projects = relationship("Project", back_populates="client", cascade="all, delete")