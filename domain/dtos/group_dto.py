from dataclasses import dataclass
from typing import Optional

@dataclass
class GroupDTO:
    id_subject: int
    id_teacher: int
    id_period: Optional[int]
    code_group: Optional[str]
    maximum_quota: Optional[str]
