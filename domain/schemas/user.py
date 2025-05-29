# core/domain/user.py
from pydantic import BaseModel, EmailStr
from datetime import date
from typing import Optional

class UserBase(BaseModel):
    tipe_document: str
    number_document: str
    name: str
    last_name: str
    phone: Optional[str] = None
    adress: Optional[str] = None
    date_of_birth: Optional[date] = None
    email: Optional[EmailStr] = None
    date_registration: Optional[date] = None
    active: Optional[bool] = True

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id_user: int

    class Config:
        orm_mode = True