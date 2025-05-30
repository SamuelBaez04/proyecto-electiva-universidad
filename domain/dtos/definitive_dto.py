from dataclasses import dataclass
from typing import Optional

@dataclass
class DefinitiveDTO:
    id_subject_inscription: int
    final_note: float
    state: Optional[str]
    observaciones: Optional[str]
