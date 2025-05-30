from dataclasses import dataclass
from typing import Optional

@dataclass
class PermissionDTO:
    name: Optional[str]
    description: Optional[str]
    code: Optional[str]
