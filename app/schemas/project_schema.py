from pydantic import BaseModel

class ProjectBase(BaseModel):
    client_id: int
    name: str
    iconUrl: str | None = None
    color: str | None = None

class ProjectCreate(ProjectBase):
    pass

class ProjectRead(ProjectBase):
    id: int

    class Config:
        orm_mode = True

class ProjectUpdate(BaseModel):
    name: str | None = None
    iconUrl: str | None = None
    color: str | None = None
    client_id: int | None = None