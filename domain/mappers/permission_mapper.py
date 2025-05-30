from domain.schemas.permission import PermissionCreate
from domain.dtos.permission_dto import PermissionDTO

def schema_to_dto(schema: PermissionCreate) -> PermissionDTO:
    return PermissionDTO(
        name=schema.name,
        description=schema.description,
        code=schema.code
    )
