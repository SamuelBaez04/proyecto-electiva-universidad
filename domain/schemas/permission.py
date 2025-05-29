# core/domain/permission.py
from pydantic import BaseModel
from typing import Optional

class PermissionBase(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    code: Optional[str] = None

class PermissionCreate(PermissionBase):
    pass

class Permission(PermissionBase):
    id_permission: int

    class Config:
        orm_mode = True