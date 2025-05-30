from domain.schemas.subject_inscription import SubjectInscriptionCreate
from domain.dtos.subject_inscription_dto import SubjectInscriptionDTO

def schema_to_dto(schema: SubjectInscriptionCreate) -> SubjectInscriptionDTO:
    return SubjectInscriptionDTO(
        id_inscription=schema.id_inscription,
        id_group=schema.id_group,
        registration_date=schema.registration_date,
        state=schema.state
    )
