
from pydantic import BaseModel
from datetime import date
from typing import Optional

class StudentBase(BaseModel):
    code_student: Optional[str] = None
    current_semester: Optional[int] = None
    academic_program: Optional[str] = None
    date_of_entry: Optional[date] = None
    state: Optional[str] = None

class StudentCreate(StudentBase):
    id_user: int

class Student(StudentBase):
    id_student: int

    class Config:
        orm_mode = True