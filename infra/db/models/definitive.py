from sqlalchemy import Column, Integer, String, DECIMAL, ForeignKey
from .base import Base

class Definitive(Base):
    __tablename__ = "definitive"
    __table_args__ = {"schema": "u"}

    id_definitive = Column(Integer, primary_key=True, autoincrement=True)
    id_subject_inscription = Column(Integer, ForeignKey("u.subject_inscription.id_subject_inscription"), nullable=False)
    final_note = Column(DECIMAL, nullable=False)
    state = Column(String(50))
    observaciones = Column(String(250))
