from sqlalchemy.orm import Session
import models, schemas

def crear_usuario(db: Session, usuario: schemas.UsuarioCreate):
    db_usuario = models.Usuario(nombre=usuario.nombre)
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

def obtener_usuarios(db: Session):
    return db.query(models.Usuario).all()

def obtener_usuario(db: Session, usuario_id: int):
    return db.query(models.Usuario).filter(models.Usuario.id == usuario_id).first()

def actualizar_estado(db: Session, usuario_id: int, estado: str):
    usuario = obtener_usuario(db, usuario_id)
    if usuario:
        usuario.estado = estado
        db.commit()
        db.refresh(usuario)
    return usuario

def hacer_premium(db: Session, usuario_id: int):
    usuario = obtener_usuario(db, usuario_id)
    if usuario:
        usuario.premium = True
        db.commit()
        db.refresh(usuario)
    return usuario

def obtener_usuarios_por_estado(db: Session, estado: str):
    return db.query(models.Usuario).filter(models.Usuario.estado == estado).all()

def obtener_usuarios_activos_premium(db: Session):
    return db.query(models.Usuario).filter(models.Usuario.estado == "Activo", models.Usuario.premium == True).all()

def crear_tarea(db: Session, tarea: schemas.TareaCreate, usuario_id: int):
    db_tarea = models.Tarea(
        descripcion=tarea.descripcion,
        estado=tarea.estado,
        usuario_id=usuario_id
    )
    db.add(db_tarea)
    db.commit()
    db.refresh(db_tarea)
    return db_tarea

def obtener_tareas(db: Session):
    return db.query(models.Tarea).all()

def obtener_tarea(db: Session, tarea_id: int):
    return db.query(models.Tarea).filter(models.Tarea.id == tarea_id).first()

def actualizar_estado_tarea(db: Session, tarea_id: int, estado: str):
    tarea = obtener_tarea(db, tarea_id)
    if tarea:
        tarea.estado = estado
        db.commit()
        db.refresh(tarea)
    return tarea

def obtener_tareas_por_estado(db: Session, estado: str):
    return db.query(models.Tarea).filter(models.Tarea.estado == estado).all()

def obtener_tareas_por_usuario(db: Session, usuario_id: int):
    return db.query(models.Tarea).filter(models.Tarea.usuario_id == usuario_id).all()
