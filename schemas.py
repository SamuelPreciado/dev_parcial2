# schemas.py

from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class UsuarioBase(BaseModel):
    nombre: str

class UsuarioCreate(UsuarioBase):
    pass

class UsuarioOut(UsuarioBase):
    id: int
    estado: str
    premium: bool

    class Config:
        from_attributes = True

class TareaBase(BaseModel):
    descripcion: str
    estado: Optional[str] = "Pendiente"

class TareaCreate(TareaBase):
    pass

class TareaOut(TareaBase):
    id: int
    usuario_id: int

    class Config:
        from_attributes = True
