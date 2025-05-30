from domain.schemas.timetable import TimetableDTO
from domain.dtos.timetable_dto import TimetableDTO as TimetableData

def schema_to_dto(schema: TimetableDTO) -> TimetableData:
    return TimetableData(
        id_group=schema.id_group,
        day=schema.day,
        start_time=schema.start_time,
        end_time=schema.end_time,
        classroom=schema.classroom,
        building=schema.building
    )
