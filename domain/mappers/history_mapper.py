from domain.schemas.inscription import InscriptionCreate
from domain.dtos.inscription_dto import InscriptionDTO

def schema_to_dto(schema: InscriptionCreate) -> InscriptionDTO:
    return InscriptionDTO(
        id_student=schema.id_student,
        id_period=schema.id_period,
        inscription_date=schema.inscription_date,
        state=schema.state,
        inscription_value=schema.inscription_value,
        inscription_type=schema.inscription_type,
        enrolled_credits=schema.enrolled_credits
    )
