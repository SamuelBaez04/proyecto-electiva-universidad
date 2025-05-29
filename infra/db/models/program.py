from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Program(Base):
    __tablename__ = "program"
    __table_args__ = {"schema": "u"}

    id_program = Column(Integer, primary_key=True, autoincrement=True)
    id_faculty = Column(Integer, ForeignKey("u.faculty.id_faculty"), nullable=False)
    name = Column(String(50))
    code = Column(String(50))
    total_credits = Column(Integer)
    semester_duration = Column(Integer)
    level = Column(String(50))
    mode = Column(String(50))

    faculty = relationship("Faculty", back_populates="programs")
