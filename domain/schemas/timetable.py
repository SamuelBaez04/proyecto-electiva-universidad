# core/domain/timetable.py
from pydantic import BaseModel
from typing import Optional

class TimetableBase(BaseModel):
    day: Optional[str] = None
    start_time: Optional[str] = None
    end_time: Optional[str] = None
    classroom: Optional[str] = None
    building: Optional[str] = None

class TimetableCreate(TimetableBase):
    id_group: int

class Timetable(TimetableBase):
    id_timetable: int

    class Config:
        orm_mode = True