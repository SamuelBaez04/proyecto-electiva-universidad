from domain.schemas.group import GroupCreate
from domain.dtos.group_dto import GroupDTO

def schema_to_dto(schema: GroupCreate) -> GroupDTO:
    return GroupDTO(
        id_subject=schema.id_subject,
        id_teacher=schema.id_teacher,
        id_period=schema.id_period,
        code_group=schema.code_group,
        maximum_quota=schema.maximum_quota
    )
