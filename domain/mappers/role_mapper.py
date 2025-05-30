from domain.schemas.role import RoleCreate
from domain.dtos.role_dto import RoleDTO

def schema_to_dto(schema: RoleCreate) -> RoleDTO:
    return RoleDTO(
        name=schema.name,
        description=schema.description
    )
