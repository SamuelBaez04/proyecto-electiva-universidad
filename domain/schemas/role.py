# core/domain/role.py
from pydantic import BaseModel
from typing import Optional

class RoleBase(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None

class RoleCreate(RoleBase):
    pass

class Role(RoleBase):
    id_rol: int

    class Config:
        orm_mode = True