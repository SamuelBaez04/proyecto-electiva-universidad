from dataclasses import dataclass
from datetime import date
from typing import Optional

@dataclass
class TeacherDTO:
    name: str
    last_name: str
    email: str
    password: str
    code_employee: Optional[str]
    speciality: Optional[str]
    type_contract: Optional[str]
    hiring_date: Optional[date]
