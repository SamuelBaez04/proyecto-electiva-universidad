from sqlalchemy.orm import Session
from domain.dtos.user_dto import UserDTO
from infra.db.models.user import User
from domain.repositories.user_repository import IUserRepository

class UserRepositorySQL(IUserRepository):
    def __init__(self, db: Session):
        self.db = db

    def create(self, dto: UserDTO) -> User:
        user = User(
            tipe_document=dto.tipe_document,
            number_document=dto.number_document,
            name=dto.name,
            last_name=dto.last_name,
            phone=dto.phone,
            adress=dto.address,
            date_of_birth=dto.date_of_birth,
            email=dto.email,
            password=dto.password,
            date_registration=dto.date_registration,
            active=dto.active
        )
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def get_by_id(self, user_id: int) -> type[User] | None:
        return self.db.query(User).filter_by(id_user=user_id).first()

    def list_all(self) -> list[type[User]]:
        return self.db.query(User).all()

    def delete(self, user_id: int) -> None:
        user = self.db.query(User).filter_by(id_user=user_id).first()
        if user:
            self.db.delete(user)
            self.db.commit()
