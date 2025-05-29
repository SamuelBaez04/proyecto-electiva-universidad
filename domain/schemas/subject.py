# core/domain/subject.py
from pydantic import BaseModel
from typing import Optional

class SubjectBase(BaseModel):
    code: str
    name: str
    description: Optional[str] = None
    credits: int
    theoretical_hours: int
    practical_hours: int
    suggested_semester: Optional[int] = None
    active: Optional[bool] = True

class SubjectCreate(SubjectBase):
    id_program: int

class Subject(SubjectBase):
    id_subject: int

    class Config:
        orm_mode = True