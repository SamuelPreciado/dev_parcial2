from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    estado = Column(String, default="Inactivo")
    premium = Column(Boolean, default=False)

    tareas = relationship("Tarea", back_populates="usuario")


class Tarea(Base):
    __tablename__ = "tareas"

    id = Column(Integer, primary_key=True, index=True)
    descripcion = Column(String, index=True)
    estado = Column(String, default="Pendiente")
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))

    usuario = relationship("Usuario", back_populates="tareas")


