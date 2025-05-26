from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import database
from app.models.project_model import Project
from app.schemas.project_schema import ProjectCreate, ProjectRead, ProjectUpdate

router = APIRouter()

@router.post("/", response_model=ProjectRead)
def create_project(project: ProjectCreate, db: Session = Depends(database.get_db)):
    db_project = Project(**project.dict())
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project

@router.get("/", response_model=list[ProjectRead])
def read_projects(db: Session = Depends(database.get_db)):
    return db.query(Project).all()

@router.get("/{project_id}", response_model=ProjectRead)
def read_project(project_id: int, db: Session = Depends(database.get_db)):
    project = db.query(Project).get(project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return project

@router.put("/{project_id}", response_model=ProjectRead)
def update_project(project_id: int, project_update: ProjectUpdate, db: Session = Depends(database.get_db)):
    project = db.query(Project).get(project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    for key, value in project_update.dict(exclude_unset=True).items():
        setattr(project, key, value)
    db.commit()
    db.refresh(project)
    return project

@router.delete("/{project_id}", status_code=204)
def delete_project(project_id: int, db: Session = Depends(database.get_db)):
    project = db.query(Project).get(project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    db.delete(project)
    db.commit()