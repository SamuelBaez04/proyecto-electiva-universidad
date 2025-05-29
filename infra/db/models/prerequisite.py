from sqlalchemy import Column, Integer, String, ForeignKey
from .base import Base

class Prerequisite(Base):
    __tablename__ = "prerequisite"
    __table_args__ = {"schema": "u"}

    id_prerequisite = Column(Integer, primary_key=True, autoincrement=True)
    id_subject = Column(Integer, ForeignKey("u.subject.id_subject"), nullable=False)
    Prerequisite_type = Column(String(45), nullable=False)
