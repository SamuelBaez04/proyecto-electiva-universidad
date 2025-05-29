from sqlalchemy import Column, Integer, String, DECIMAL, ForeignKey
from .base import Base

class HistoryAcademic(Base):
    __tablename__ = "history_academic"
    __table_args__ = {"schema": "u"}

    id_history = Column(Integer, primary_key=True, autoincrement=True)
    id_estudent = Column(Integer, ForeignKey("u.student.id_student"), nullable=False)
    id_period = Column(Integer, ForeignKey("u.academic_period.id_period"), nullable=False)
    average_semester = Column(DECIMAL(10, 2))
    average_accumulator = Column(DECIMAL(10, 2))
    credits_aproved = Column(String(45))
    credits_courses = Column(String(45))
    status_academic = Column(String(100))
