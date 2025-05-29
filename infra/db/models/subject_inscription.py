from sqlalchemy import Column, Integer, String, Date, ForeignKey
from .base import Base

class SubjectInscription(Base):
    __tablename__ = "subject_inscription"
    __table_args__ = {"schema": "u"}

    id_subject_inscription = Column(Integer, primary_key=True, autoincrement=True)
    id_inscription = Column(Integer, ForeignKey("u.inscription.id_inscription"), nullable=False)
    id_group = Column(Integer, ForeignKey("u.group.id_group"), nullable=False)
    registration_date = Column(Date)
    state = Column(String(45))
