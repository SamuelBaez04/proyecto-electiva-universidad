from domain.schemas.teacher import TeacherCreate
from domain.dtos.teacher_dto import TeacherDTO
from infra.db.models.teacher import Teacher
from infra.db.models.user import User

def schema_to_dto(schema: TeacherCreate) -> TeacherDTO:
    return TeacherDTO(
        name=schema.user.name,
        last_name=schema.user.last_name,
        email=schema.user.email,
        password=schema.password,
        code_employee=schema.teacher.code_employee,
        speciality=schema.teacher.speciality,
        type_contract=schema.teacher.type_contract,
        hiring_date=schema.teacher.hiring_date
    )

def orm_to_dto(teacher: Teacher, user: User) -> TeacherDTO:
    return TeacherDTO(
        name=user.name,
        last_name=user.last_name,
        email=user.email,
        password=user.password,
        code_employee=teacher.code_employee,
        speciality=teacher.speciality,
        type_contract=teacher.type_contract,
        hiring_date=teacher.hiring_date
    )
