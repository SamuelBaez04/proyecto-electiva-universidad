from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Teacher(Base):
    __tablename__ = "teacher"
    __table_args__ = {"schema": "u"}

    id_teacher = Column(Integer, primary_key=True, autoincrement=True)
    id_user = Column(Integer, ForeignKey("u.user.id_user"), nullable=False)
    code_employee = Column(String(45))
    speciality = Column(String(45))
    type_contract = Column(String(45))
    hiring_date = Column(Date)

    user = relationship("User", back_populates="teacher")
