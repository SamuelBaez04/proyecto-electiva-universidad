from domain.schemas.user_role import UserRoleCreate
from domain.dtos.user_role_dto import UserRoleDTO

def schema_to_dto(schema: UserRoleCreate) -> UserRoleDTO:
    return UserRoleDTO(
        id_user=schema.id_user,
        id_rol=schema.id_rol,
        assignment_date=schema.assignment_date
    )
