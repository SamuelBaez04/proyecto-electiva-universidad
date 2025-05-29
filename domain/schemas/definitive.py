from pydantic import BaseModel
from typing import Optional

class DefinitiveBase(BaseModel):
    final_note: float
    state: Optional[str] = None
    observaciones: Optional[str] = None

class DefinitiveCreate(DefinitiveBase):
    id_subject_inscription: int

class Definitive(DefinitiveBase):
    id_definitive: int

    class Config:
        orm_mode = True