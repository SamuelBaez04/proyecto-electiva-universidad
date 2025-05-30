from dataclasses import dataclass
from datetime import date
from typing import Optional

@dataclass
class AcademicPeriodDTO:
    name: Optional[str]
    start_date: Optional[date]
    end_date: Optional[date]
    state: Optional[str]
    year: Optional[int]
    semester: Optional[int]
