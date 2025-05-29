from pydantic import BaseModel
from typing import Optional

class FacultyBase(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    code: Optional[str] = None

class FacultyCreate(FacultyBase):
    pass

class Faculty(FacultyBase):
    id_faculty: int

    class Config:
        orm_mode = True