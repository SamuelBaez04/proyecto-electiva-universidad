# core/domain/teacher.py
from pydantic import BaseModel
from datetime import date
from typing import Optional

class TeacherBase(BaseModel):
    code_employee: Optional[str] = None
    speciality: Optional[str] = None
    type_contract: Optional[str] = None
    hiring_date: Optional[date] = None

class TeacherCreate(TeacherBase):
    id_user: int

class Teacher(TeacherBase):
    id_teacher: int

    class Config:
        orm_mode = True