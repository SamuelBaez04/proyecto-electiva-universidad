from dataclasses import dataclass
from typing import Optional
from datetime import time

@dataclass
class TimetableDTO:
    id_group: int
    day: Optional[str]
    start_time: Optional[time]
    end_time: Optional[time]
    classroom: Optional[str]
    building: Optional[str]
