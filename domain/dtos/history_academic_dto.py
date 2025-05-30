from dataclasses import dataclass
from typing import Optional

@dataclass
class HistoryAcademicDTO:
    id_estudent: int
    id_period: int
    average_semester: Optional[float]
    average_accumulator: Optional[float]
    credits_aproved: Optional[str]
    credits_courses: Optional[str]
    status_academic: Optional[str]
