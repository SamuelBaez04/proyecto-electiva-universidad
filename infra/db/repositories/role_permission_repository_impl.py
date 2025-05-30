from sqlalchemy.orm import Session
from domain.dtos.role_permission_dto import RolePermissionDTO
from infra.db.models.role_permission import RolePermission
from domain.repositories.role_permission_repository import IRolePermissionRepository

class RolPermissionRepositorySQL(IRolePermissionRepository):
    def __init__(self, db: Session):
        self.db = db

    def create(self, dto: RolePermissionDTO) -> RolePermission:
        entity = RolePermission(
            id_rol=dto.id_rol,
            id_permission=dto.id_permission
        )
        self.db.add(entity)
        self.db.commit()
        self.db.refresh(entity)
        return entity

    def get_all(self) -> list[type[RolePermission]]:
        return self.db.query(RolePermission).all()

    def delete(self, id_rol_permission: int) -> None:
        entity = self.db.query(RolePermission).filter_by(id_rol_Permission=id_rol_permission).first()
        if entity:
            self.db.delete(entity)
            self.db.commit()
