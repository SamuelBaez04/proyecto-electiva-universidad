from pydantic import BaseModel
from datetime import date
from typing import Optional

class AcademicPeriodBase(BaseModel):
    name: Optional[str] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    state: Optional[str] = None
    year: Optional[int] = None
    semester: Optional[int] = None

class AcademicPeriodCreate(AcademicPeriodBase):
    pass

class AcademicPeriod(AcademicPeriodBase):
    id_period: int

    class Config:
        orm_mode = True