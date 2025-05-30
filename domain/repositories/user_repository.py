from abc import ABC, abstractmethod
from typing import List
from domain.dtos.user_dto import UserDTO
from infra.db.models.user import User

class IUserRepository(ABC):

    @abstractmethod
    def create(self, dto: UserDTO) -> User:
        pass

    @abstractmethod
    def get_by_id(self, user_id: int) -> User:
        pass

    @abstractmethod
    def list_all(self) -> List[User]:
        pass

    @abstractmethod
    def delete(self, user_id: int) -> None:
        pass
