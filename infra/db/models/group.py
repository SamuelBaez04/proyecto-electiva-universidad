from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Group(Base):
    __tablename__ = "group"
    __table_args__ = {"schema": "u"}

    id_group = Column(Integer, primary_key=True, autoincrement=True)
    id_subject = Column(Integer, ForeignKey("u.subject.id_subject"), nullable=False)
    id_teacher = Column(Integer, ForeignKey("u.teacher.id_teacher"), nullable=False)
    id_period = Column(Integer, ForeignKey("u.academic_period.id_period"))
    code_group = Column(String(45))
    maximum_quota = Column(String(45))

    subject = relationship("Subject")
    teacher = relationship("Teacher")
    academic_period = relationship("AcademicPeriod")
