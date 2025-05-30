from dataclasses import dataclass
from typing import Optional

@dataclass
class ProgramDTO:
    id_faculty: int
    name: Optional[str]
    code: Optional[str]
    total_credits: Optional[int]
    semester_duration: Optional[int]
    level: Optional[str]
    mode: Optional[str]
