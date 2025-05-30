from dataclasses import dataclass
from typing import Optional
from datetime import date

@dataclass
class UserDTO:
    tipe_document: Optional[str]
    number_document: Optional[str]
    name: Optional[str]
    last_name: Optional[str]
    phone: Optional[str]
    address: Optional[str]
    date_of_birth: Optional[date]
    email: Optional[str]
    password: str
    date_registration: Optional[date]
    active: Optional[bool]
