from pydantic import BaseModel

class UsuarioBase(BaseModel):
    nombre: str

class UsuarioCreate(UsuarioBase):
    pass

class UsuarioOut(UsuarioBase):
    id: int
    estado: str
    premium: bool

    class Config:
        orm_mode = True
