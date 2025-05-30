from domain.schemas.faculty import FacultyCreate
from domain.dtos.faculty_dto import FacultyDTO

def schema_to_dto(schema: FacultyCreate) -> FacultyDTO:
    return FacultyDTO(
        name=schema.name,
        description=schema.description,
        code=schema.code
    )
