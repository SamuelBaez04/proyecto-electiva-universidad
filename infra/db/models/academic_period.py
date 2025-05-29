from sqlalchemy import Column, Integer, String, Date
from .base import Base

class AcademicPeriod(Base):
    __tablename__ = "academic_period"
    __table_args__ = {"schema": "u"}

    id_period = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    start_date = Column(Date)
    end_date = Column(Date)
    state = Column(String(45))
    year = Column(Integer)
    semester = Column(Integer)
