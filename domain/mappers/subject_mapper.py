from domain.schemas.subject import SubjectCreate
from domain.dtos.subject_dto import SubjectDTO

def schema_to_dto(schema: SubjectCreate) -> SubjectDTO:
    return SubjectDTO(
        id_program=schema.id_program,
        code=schema.code,
        name=schema.name,
        description=schema.description,
        credits=schema.credits,
        theoretical_hours=schema.theoretical_hours,
        practical_hours=schema.practical_hours,
        suggested_semester=schema.suggested_semester,
        active=schema.active
    )
