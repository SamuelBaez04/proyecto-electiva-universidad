from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from .base import Base

class Subject(Base):
    __tablename__ = "subject"
    __table_args__ = {"schema": "u"}

    id_subject = Column(Integer, primary_key=True, autoincrement=True)
    id_program = Column(Integer, ForeignKey("u.program.id_program"), nullable=False)
    code = Column(String(50), nullable=False)
    name = Column(String(100), nullable=False)
    description = Column(String(250))
    credits = Column(Integer, nullable=False)
    theoretical_hours = Column(Integer, nullable=False)
    practical_hours = Column(Integer, nullable=False)
    suggested_semester = Column(Integer)
    active = Column(Boolean)

    program = relationship("Program")
