from fastapi import FastAPI
from app.routers import tasks
from app.database import create_tables

app = FastAPI(title="Task Manager API")

# Crear las tablas al iniciar (solo si no existen)
create_tables()

# Incluir rutas
app.include_router(tasks.router, prefix="/tasks", tags=["Tasks"])
