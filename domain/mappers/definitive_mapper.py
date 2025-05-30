from domain.schemas.definitive import DefinitiveCreate
from domain.dtos.definitive_dto import DefinitiveDTO

def schema_to_dto(schema: DefinitiveCreate) -> DefinitiveDTO:
    return DefinitiveDTO(
        id_subject_inscription=schema.id_subject_inscription,
        final_note=schema.final_note,
        state=schema.state,
        observaciones=schema.observaciones
    )
