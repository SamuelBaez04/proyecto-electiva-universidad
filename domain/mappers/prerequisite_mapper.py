from domain.schemas.prerequisite import PrerequisiteCreate
from domain.dtos.prerequisite_dto import PrerequisiteDTO

def schema_to_dto(schema: PrerequisiteCreate) -> PrerequisiteDTO:
    return PrerequisiteDTO(
        id_subject=schema.id_subject,
        Prerequisite_type=schema.Prerequisite_type
    )
