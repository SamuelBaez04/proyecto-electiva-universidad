from typing import Any, Coroutine

from sqlalchemy.orm import Session
from domain.dtos.student_dto import StudentDTO
from infra.db.models.student import Student
from infra.db.models.user import User

class StudentRepository:
    def __init__(self, db: Session):
        self.db = db

    async def create(self, dto: StudentDTO) -> Student:
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

    async def get_by_id(self, id_student: int) -> type[Student] | None:
        return self.db.query(Student).filter_by(id_student=id_student).first()

    async def list_all(self) -> list[type[Student]]:
        return self.db.query(Student).all()

    async def delete(self, id_student: int) -> None:
        student = self.db.query(Student).filter_by(id_student=id_student).first()
        if student:
            self.db.delete(student)
            self.db.commit()
