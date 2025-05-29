from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Student(Base):
    __tablename__ = "student"
    __table_args__ = {"schema": "u"}

    id_student = Column(Integer, primary_key=True, autoincrement=True)
    id_user = Column(Integer, ForeignKey("u.user.id_user"), nullable=False)
    code_student = Column(String(45))
    current_semester = Column(Integer)
    academinc_program = Column(String(45))
    date_of_entry = Column(Date)
    state = Column(String(45))

    user = relationship("User", back_populates="student")
