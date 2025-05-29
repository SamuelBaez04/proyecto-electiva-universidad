# core/domain/subject_inscription.py
from pydantic import BaseModel
from datetime import date
from typing import Optional

class SubjectInscriptionBase(BaseModel):
    registration_date: Optional[date] = None
    state: Optional[str] = None

class SubjectInscriptionCreate(SubjectInscriptionBase):
    id_inscription: int
    id_group: int

class SubjectInscription(SubjectInscriptionBase):
    id_subject_inscription: int

    class Config:
        orm_mode = True