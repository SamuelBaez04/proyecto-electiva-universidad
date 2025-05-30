from domain.schemas.user import UserCreate
from domain.dtos.user_dto import UserDTO

def schema_to_dto(schema: UserCreate) -> UserDTO:
    return UserDTO(
        tipe_document=schema.tipe_document,
        number_document=schema.number_document,
        name=schema.name,
        last_name=schema.last_name,
        phone=schema.phone,
        adress=schema.adress,
        date_of_birth=schema.date_of_birth,
        email=schema.email,
        password=schema.password,
        date_registration=schema.date_registration,
        active=schema.active
    )
