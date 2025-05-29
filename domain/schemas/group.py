from pydantic import BaseModel
from typing import Optional

class GroupBase(BaseModel):
    code_group: Optional[str] = None
    maximum_quota: Optional[str] = None

class GroupCreate(GroupBase):
    id_subject: int
    id_teacher: int
    id_period: Optional[int] = None

class Group(GroupBase):
    id_group: int

    class Config:
        orm_mode = True