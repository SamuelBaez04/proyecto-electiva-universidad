from abc import ABC, abstractmethod
from typing import List
from domain.dtos.teacher_dto import TeacherDTO
from infra.db.models.teacher import Teacher

class ITeacherRepository(ABC):

    @abstractmethod
    def create(self, dto: TeacherDTO) -> Teacher:
        pass

    @abstractmethod
    def get_by_id(self, teacher_id: int) -> Teacher:
        pass

    @abstractmethod
    def list_all(self) -> List[Teacher]:
        pass

    @abstractmethod
    def delete(self, teacher_id: int) -> None:
        pass
