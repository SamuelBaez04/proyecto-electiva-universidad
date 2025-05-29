from sqlalchemy import Column, Integer, String, Date, DECIMAL, ForeignKey
from .base import Base

class Grade(Base):
    __tablename__ = "grade"
    __table_args__ = {"schema": "u"}

    id_grade = Column(Integer, primary_key=True, autoincrement=True)
    id_subject_inscription = Column(Integer, ForeignKey("u.subject_inscription.id_subject_inscription"), nullable=False)
    evaluation_type = Column(String(45))
    grade_value = Column(DECIMAL)
    percentage = Column(DECIMAL)
    registration_date = Column(Date)
    observations = Column(String(45))
