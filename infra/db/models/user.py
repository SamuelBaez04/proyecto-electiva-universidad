from sqlalchemy import Column, Integer, String, Date, Boolean
from sqlalchemy.orm import relationship
from .base import Base

class User(Base):
    __tablename__ = "user"
    __table_args__ = {"schema": "u"}

    id_user = Column(Integer, primary_key=True, autoincrement=True)
    tipe_document = Column(String(100))
    number_document = Column(String(45))
    name = Column(String(100))
    last_name = Column(String(100))
    phone = Column(String(10))
    adress = Column(String(45))
    date_of_birth = Column(Date)
    email = Column(String(50))
    password = Column(String(15), nullable=False)
    date_registration = Column(Date)
    active = Column(Boolean)

    student = relationship("Student", back_populates="user", uselist=False)
    teacher = relationship("Teacher", back_populates="user", uselist=False)
    roles = relationship("UserRole", back_populates="user")
