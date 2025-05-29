# core/domain/prerequisite.py
from pydantic import BaseModel

class PrerequisiteBase(BaseModel):
    Prerequisite_type: str

class PrerequisiteCreate(PrerequisiteBase):
    id_subject: int

class Prerequisite(PrerequisiteBase):
    id_prerequisite: int

    class Config:
        orm_mode = True