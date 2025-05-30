from dataclasses import dataclass
from datetime import date
from typing import Optional

@dataclass
class SubjectInscriptionDTO:
    id_inscription: int
    id_group: int
    registration_date: Optional[date]
    state: Optional[str]
