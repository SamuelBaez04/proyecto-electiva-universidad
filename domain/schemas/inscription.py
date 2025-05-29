# core/domain/inscription.py
from pydantic import BaseModel
from datetime import date
from typing import Optional

class InscriptionBase(BaseModel):
    inscription_date: Optional[date] = None
    state: Optional[str] = None
    inscription_value: Optional[float] = None
    inscription_type: Optional[str] = None
    enrolled_credits: Optional[int] = None

class InscriptionCreate(InscriptionBase):
    id_student: int
    id_period: int

class Inscription(InscriptionBase):
    id_inscription: int

    class Config:
        orm_mode = True