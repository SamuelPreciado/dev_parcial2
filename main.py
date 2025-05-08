from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import List

import crud, models, schemas
from database import engine, SessionLocal
from sqlalchemy.orm import Session
from fastapi import Depends

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="API de Usuarios")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/usuarios/", response_model=schemas.UsuarioOut)
def crear_usuario(usuario: schemas.UsuarioCreate, db: Session = Depends(get_db)):
    return crud.crear_usuario(db, usuario)

@app.get("/usuarios/", response_model=List[schemas.UsuarioOut])
def listar_usuarios(db: Session = Depends(get_db)):
    return crud.obtener_usuarios(db)

@app.get("/usuarios/activos_premium", response_model=List[schemas.UsuarioOut])
def listar_activos_premium(db: Session = Depends(get_db)):
    return crud.obtener_usuarios_activos_premium(db)

@app.get("/usuarios/activos", response_model=List[schemas.UsuarioOut])
def listar_activos(db: Session = Depends(get_db)):
    return crud.obtener_usuarios_por_estado(db, "Activo")

@app.get("/usuarios/{usuario_id}", response_model=schemas.UsuarioOut)
def obtener_usuario(usuario_id: int, db: Session = Depends(get_db)):
    return crud.obtener_usuario(db, usuario_id)

@app.patch("/usuarios/{usuario_id}/estado", response_model=schemas.UsuarioOut)
def actualizar_estado(usuario_id: int, estado: str, db: Session = Depends(get_db)):
    return crud.actualizar_estado(db, usuario_id, estado)

@app.patch("/usuarios/{usuario_id}/premium", response_model=schemas.UsuarioOut)
def hacer_premium(usuario_id: int, db: Session = Depends(get_db)):
    return crud.hacer_premium(db, usuario_id)

@app.post("/tareas/", response_model=schemas.TareaOut)
def crear_tarea(tarea: schemas.TareaCreate, usuario_id: int, db: Session = Depends(get_db)):
    return crud.crear_tarea(db, tarea, usuario_id)

@app.get("/tareas/", response_model=List[schemas.TareaOut])
def listar_tareas(db: Session = Depends(get_db)):
    return crud.obtener_tareas(db)

@app.get("/tareas/{tarea_id}", response_model=schemas.TareaOut)
def obtener_tarea(tarea_id: int, db: Session = Depends(get_db)):
    tarea = crud.obtener_tarea(db, tarea_id)
    if tarea is None:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return tarea

@app.patch("/tareas/{tarea_id}/estado", response_model=schemas.TareaOut)
def actualizar_estado_tarea(tarea_id: int, estado: str, db: Session = Depends(get_db)):
    tarea = crud.actualizar_estado_tarea(db, tarea_id, estado)
    if tarea is None:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return tarea

@app.get("/tareas/estado/{estado}", response_model=List[schemas.TareaOut])
def listar_tareas_por_estado(estado: str, db: Session = Depends(get_db)):
    return crud.obtener_tareas_por_estado(db, estado)

@app.get("/tareas/usuario/{usuario_id}", response_model=List[schemas.TareaOut])
def listar_tareas_por_usuario(usuario_id: int, db: Session = Depends(get_db)):
    return crud.obtener_tareas_por_usuario(db, usuario_id)
