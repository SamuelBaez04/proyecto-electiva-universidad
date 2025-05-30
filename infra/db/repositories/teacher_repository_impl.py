from sqlalchemy.orm import Session
from domain.dtos.teacher_dto import TeacherDTO
from infra.db.models.teacher import Teacher
from infra.db.models.user import User
from domain.repositories.teacher_repository import ITeacherRepository

class TeacherRepositorySQL(ITeacherRepository):
    def __init__(self, db: Session):
        self.db = db

    def create(self, dto: TeacherDTO) -> Teacher:
        user = User(
            name=dto.name,
            last_name=dto.last_name,
            email=dto.email,
            password=dto.password
        )
        self.db.add(user)
        self.db.flush()  # Obtener id_user

        teacher = Teacher(
            id_user=user.id_user,
            code_employee=dto.code_employee,
            speciality=dto.speciality,
            type_contract=dto.type_contract,
            hiring_date=dto.hiring_date
        )
        self.db.add(teacher)
        self.db.commit()
        self.db.refresh(teacher)
        return teacher

    def get_by_id(self, teacher_id: int) -> type[Teacher] | None:
        return self.db.query(Teacher).filter_by(id_teacher=teacher_id).first()

    def list_all(self) -> list[type[Teacher]]:
        return self.db.query(Teacher).all()

    def delete(self, teacher_id: int) -> None:
        teacher = self.db.query(Teacher).filter_by(id_teacher=teacher_id).first()
        if teacher:
            self.db.delete(teacher)
            self.db.commit()
