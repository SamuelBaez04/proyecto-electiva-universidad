from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class RolPermission(Base):
    __tablename__ = "rol_permission"
    __table_args__ = {"schema": "u"}

    id_rol_Permission = Column(Integer, primary_key=True)
    id_rol = Column(Integer, ForeignKey("u.rol.id_rol"), nullable=False)
    id_permission = Column(Integer, ForeignKey("u.permission.id_permission"), nullable=False)

    rol = relationship("Rol", back_populates="permissions")
    permission = relationship("Permission", back_populates="roles")
