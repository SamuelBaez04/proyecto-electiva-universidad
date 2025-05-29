from pydantic import BaseModel
from datetime import date
from typing import Optional

class GradeBase(BaseModel):
    evaluation_type: Optional[str] = None
    grade_value: Optional[float] = None
    percentage: Optional[float] = None
    registration_date: Optional[date] = None
    observations: Optional[str] = None

class GradeCreate(GradeBase):
    id_subject_inscription: int

class Grade(GradeBase):
    id_grade: int

    class Config:
        orm_mode = True