from pydantic import BaseModel
from typing import Optional

class RolePermissionBase(BaseModel):
    id_role: Optional[int] = None
    id_permission: Optional[int] = None

class RolePermissionCreate(BaseModel):
    pass

class RolePermission(BaseModel):
    id_role: id
    id_permission: id

    class Config:
        orm_mode = True
