# core/domain/user_role.py
from pydantic import BaseModel
from datetime import date
from typing import Optional

class UserRoleBase(BaseModel):
    assignment_date: Optional[date] = None

class UserRoleCreate(UserRoleBase):
    id_user: int
    id_rol: int

class UserRole(UserRoleBase):
    id_user_role: int

    class Config:
        orm_mode = True