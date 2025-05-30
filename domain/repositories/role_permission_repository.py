from abc import ABC, abstractmethod
from typing import List
from domain.dtos.role_permission_dto import RolePermissionDTO
from infra.db.models.role_permission import RolePermission

class IRolePermissionRepository(ABC):

    @abstractmethod
    def create(self, dto: RolePermissionDTO) -> RolePermission:
        pass

    @abstractmethod
    def get_all(self) -> List[RolePermission]:
        pass

    @abstractmethod
    def delete(self, id_rol_permission: int) -> None:
        pass
