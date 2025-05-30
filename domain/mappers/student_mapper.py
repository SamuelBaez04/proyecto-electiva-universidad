from domain.schemas.student import StudentCreate
from domain.dtos.student_dto import StudentDTO

def schema_to_dto(schema: StudentCreate) -> StudentDTO:
    return StudentDTO(
        name=schema.user.name,
        last_name=schema.user.last_name,
        email=schema.user.email,
        password=schema.password,
        code_student=schema.student.code_student,
        current_semester=schema.student.current_semester,
        academinc_program=schema.student.academinc_program,
        date_of_entry=schema.student.date_of_entry,
        state=schema.student.state
    )
