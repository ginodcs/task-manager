from pydantic import BaseModel

class ClientBase(BaseModel):
    name: str
    logoUrl: str | None = None

class ClientCreate(ClientBase):
    pass

class ClientRead(ClientBase):
    id: int

    class Config:
        orm_mode = True

class ClientUpdate(BaseModel):
    name: str | None = None
    logoUrl: str | None = None