from dataclasses import dataclass
from datetime import date
from typing import Optional

@dataclass
class InscriptionDTO:
    id_student: int
    id_period: int
    inscription_date: Optional[date]
    state: Optional[str]
    inscription_value: Optional[float]
    inscription_type: Optional[str]
    enrolled_credits: Optional[int]
