# core/domain/history_academic.py
from pydantic import BaseModel
from typing import Optional

class HistoryAcademicBase(BaseModel):
    average_semester: Optional[float] = None
    average_accumulator: Optional[float] = None
    credits_aproved: Optional[str] = None
    credits_courses: Optional[str] = None
    status_academic: Optional[str] = None

class HistoryAcademicCreate(HistoryAcademicBase):
    id_estudent: int
    id_period: int

class HistoryAcademic(HistoryAcademicBase):
    id_history: int

    class Config:
        orm_mode = True