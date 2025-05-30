from domain.schemas.academic_period import AcademicPeriodCreate
from domain.dtos.academic_period_dto import AcademicPeriodDTO

def schema_to_dto(schema: AcademicPeriodCreate) -> AcademicPeriodDTO:
    return AcademicPeriodDTO(
        name=schema.name,
        start_date=schema.start_date,
        end_date=schema.end_date,
        state=schema.state,
        year=schema.year,
        semester=schema.semester
    )
