from domain.schemas.program import ProgramCreate
from domain.dtos.program_dto import ProgramDTO

def schema_to_dto(schema: ProgramCreate) -> ProgramDTO:
    return ProgramDTO(
        id_faculty=schema.id_faculty,
        name=schema.name,
        code=schema.code,
        total_credits=schema.total_credits,
        semester_duration=schema.semester_duration,
        level=schema.level,
        mode=schema.mode
    )
