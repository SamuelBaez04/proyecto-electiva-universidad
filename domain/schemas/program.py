# core/domain/program.py
from pydantic import BaseModel
from typing import Optional

class ProgramBase(BaseModel):
    name: Optional[str] = None
    code: Optional[str] = None
    total_credits: Optional[int] = None
    semester_duration: Optional[int] = None
    level: Optional[str] = None
    mode: Optional[str] = None

class ProgramCreate(ProgramBase):
    id_faculty: int

class Program(ProgramBase):
    id_program: int

    class Config:
        orm_mode = True