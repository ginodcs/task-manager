from fastapi import FastAPI
from app.routers import clients_router
from app.routers import projects_router
from app.routers import tasks_router
from app.database import create_tables

app = FastAPI(title="Task Manager API")

# Crear las tablas al iniciar (solo si no existen)
create_tables()

# Incluir rutas
app.include_router(clients_router.router, prefix="/clients", tags=["Clients"])
app.include_router(projects_router.router, prefix="/projects", tags=["Projects"])
app.include_router(tasks_router.router, prefix="/tasks", tags=["Tasks"])
