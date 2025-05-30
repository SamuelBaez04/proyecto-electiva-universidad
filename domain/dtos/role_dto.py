from dataclasses import dataclass
from typing import Optional

@dataclass
class RoleDTO:
    name: Optional[str]
    description: Optional[str]
