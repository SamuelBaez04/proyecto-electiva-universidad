from dataclasses import dataclass
from typing import Optional

@dataclass
class FacultyDTO:
    name: Optional[str]
    description: Optional[str]
    code: Optional[str]
