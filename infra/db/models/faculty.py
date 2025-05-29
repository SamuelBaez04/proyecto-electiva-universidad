from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base

class Faculty(Base):
    __tablename__ = "faculty"
    __table_args__ = {"schema": "u"}

    id_faculty = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    description = Column(String(250))
    code = Column(String(50))

    programs = relationship("Program", back_populates="faculty")
