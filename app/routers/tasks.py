from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import database
from app.models import task_model
from app.schemas import task_schema

router = APIRouter()

@router.post("/", response_model=task_schema.TaskRead)
def create_task(task: task_schema.TaskCreate, db: Session = Depends(database.get_db)):
    db_task = task_model.Task(**task.dict())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

@router.get("/", response_model=list[task_schema.TaskRead])
def read_tasks(db: Session = Depends(database.get_db)):
    return db.query(task_model.Task).all()

@router.get("/{task_id}", response_model=task_schema.TaskRead)
def read_task(task_id: int, db: Session = Depends(database.get_db)):
    task = db.query(task_model.Task).get(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.put("/{task_id}", response_model=task_schema.TaskRead)
def update_task(task_id: int, task_update: task_schema.TaskUpdate, db: Session = Depends(database.get_db)):
    task = db.query(task_model.Task).get(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    for key, value in task_update.dict(exclude_unset=True).items():
        setattr(task, key, value)
    
    db.commit()
    db.refresh(task)
    return task

@router.delete("/{task_id}", status_code=204)
def delete_task(task_id: int, db: Session = Depends(database.get_db)):
    task = db.query(task_model.Task).get(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    db.delete(task)
    db.commit()
