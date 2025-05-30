from domain.schemas.history_academic import HistoryAcademicCreate
from domain.dtos.history_academic_dto import HistoryAcademicDTO

def schema_to_dto(schema: HistoryAcademicCreate) -> HistoryAcademicDTO:
    return HistoryAcademicDTO(
        id_estudent=schema.id_estudent,
        id_period=schema.id_period,
        average_semester=schema.average_semester,
        average_accumulator=schema.average_accumulator,
        credits_aproved=schema.credits_aproved,
        credits_courses=schema.credits_courses,
        status_academic=schema.status_academic
    )
