from sqlalchemy.orm import Session
from domain.dtos.student_dto import StudentDTO
from infra.db.models.student import Student
from infra.db.models.user import User
from domain.repositories.student_repository import IStudentRepository

class StudentRepositorySQL(IStudentRepository):
    def __init__(self, db: Session):
        self.db = db

    def create(self, dto: StudentDTO) -> Student:
        user = User(
            name=dto.name,
            last_name=dto.last_name,
            email=dto.email,
            password=dto.password
        )
        self.db.add(user)
        self.db.flush()

        student = Student(
            id_user=user.id_user,
            code_student=dto.code_student,
            current_semester=dto.current_semester,
            academinc_program=dto.academic_program,
            date_of_entry=dto.date_of_entry,
            state=dto.state
        )
        self.db.add(student)
        self.db.commit()
        self.db.refresh(student)
        return student

    def get_by_id(self, student_id: int) -> type[Student] | None:
        return self.db.query(Student).filter_by(id_student=student_id).first()

    def list_all(self) -> list[type[Student]]:
        return self.db.query(Student).all()

    def delete(self, student_id: int) -> None:
        student = self.db.query(Student).filter_by(id_student=student_id).first()
        if student:
            self.db.delete(student)
            self.db.commit()
