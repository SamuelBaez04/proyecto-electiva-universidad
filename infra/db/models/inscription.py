from sqlalchemy import Column, Integer, String, Date, DECIMAL, ForeignKey
from .base import Base

class Inscription(Base):
    __tablename__ = "inscription"
    __table_args__ = {"schema": "u"}

    id_inscription = Column(Integer, primary_key=True, autoincrement=True)
    id_student = Column(Integer, ForeignKey("u.student.id_student"), nullable=False)
    id_period = Column(Integer, ForeignKey("u.academic_period.id_period"), nullable=False)
    inscription_date = Column(Date)
    state = Column(String(50))
    inscription_value = Column(DECIMAL(10, 2))
    inscription_type = Column(String(50))
    enrolled_credits = Column(Integer)
