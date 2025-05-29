from sqlalchemy import Column, Integer, String, Time, ForeignKey
from .base import Base

class Timetable(Base):
    __tablename__ = "timetable"
    __table_args__ = {"schema": "u"}

    id_timetable = Column(Integer, primary_key=True, autoincrement=True)
    id_group = Column(Integer, ForeignKey("u.group.id_group"), nullable=False)
    day = Column(String(45))
    start_time = Column(Time)
    end_time = Column(Time)
    classroom = Column(String(45))
    building = Column(String(45))
