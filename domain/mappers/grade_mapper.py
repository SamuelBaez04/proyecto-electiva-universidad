from domain.schemas.grade import GradeCreate
from domain.dtos.grade_dto import GradeDTO

def schema_to_dto(schema: GradeCreate) -> GradeDTO:
    return GradeDTO(
        id_subject_inscription=schema.id_subject_inscription,
        evaluation_type=schema.evaluation_type,
        grade_value=schema.grade_value,
        percentage=schema.percentage,
        registration_date=schema.registration_date,
        observations=schema.observations
    )
