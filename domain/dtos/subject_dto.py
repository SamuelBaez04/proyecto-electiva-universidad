from dataclasses import dataclass
from typing import Optional

@dataclass
class SubjectDTO:
    id_program: int
    code: str
    name: str
    description: Optional[str]
    credits: int
    theoretical_hours: int
    practical_hours: int
    suggested_semester: Optional[int]
    active: Optional[bool]
