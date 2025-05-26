from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import database
from app.models.client_model import Client
from app.schemas.client_schema import ClientCreate, ClientRead, ClientUpdate

router = APIRouter()

@router.post("/", response_model=ClientRead)
def create_client(client: ClientCreate, db: Session = Depends(database.get_db)):
    db_client = Client(**client.dict())
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client

@router.get("/", response_model=list[ClientRead])
def read_clients(db: Session = Depends(database.get_db)):
    return db.query(Client).all()

@router.get("/{client_id}", response_model=ClientRead)
def read_client(client_id: int, db: Session = Depends(database.get_db)):
    client = db.query(Client).get(client_id)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    return client

@router.put("/{client_id}", response_model=ClientRead)
def update_client(client_id: int, client_update: ClientUpdate, db: Session = Depends(database.get_db)):
    client = db.query(Client).get(client_id)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    for key, value in client_update.dict(exclude_unset=True).items():
        setattr(client, key, value)
    db.commit()
    db.refresh(client)
    return client

@router.delete("/{client_id}", status_code=204)
def delete_client(client_id: int, db: Session = Depends(database.get_db)):
    client = db.query(Client).get(client_id)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    db.delete(client)
    db.commit()