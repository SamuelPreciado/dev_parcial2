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
