from dataclasses import dataclass
from datetime import date
from typing import Optional

@dataclass
class GradeDTO:
    id_subject_inscription: int
    evaluation_type: Optional[str]
    grade_value: Optional[float]
    percentage: Optional[float]
    registration_date: Optional[date]
    observations: Optional[str]
