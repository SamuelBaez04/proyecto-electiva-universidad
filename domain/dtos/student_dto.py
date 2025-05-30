from dataclasses import dataclass
from datetime import date
from typing import Optional

@dataclass
class StudentDTO:
    name: str
    last_name: str
    email: str
    password: str
    code_student: Optional[str]
    current_semester: Optional[int]
    academinc_program: Optional[str]
    date_of_entry: Optional[date]
    state: Optional[str]
