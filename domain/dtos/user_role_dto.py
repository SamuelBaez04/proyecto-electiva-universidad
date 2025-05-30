from dataclasses import dataclass
from typing import Optional
from datetime import date

@dataclass
class UserRoleDTO:
    id_user: int
    id_rol: int
    assignment_date: Optional[date]
