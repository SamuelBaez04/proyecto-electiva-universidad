from domain.schemas.role_permission import RolePermissionCreate
from domain.dtos.role_permission_dto import RolePermissionDTO

def schema_to_dto(schema: RolePermissionCreate) -> RolePermissionDTO:
    return RolePermissionDTO(
        id_rol=schema.id_rol,
        id_permission=schema.id_permission
    )
