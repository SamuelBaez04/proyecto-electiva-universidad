from abc import ABC, abstractmethod
from typing import List
from domain.dtos.student_dto import StudentDTO
from infra.db.models.student import Student

class IStudentRepository(ABC):

    @abstractmethod
    def create(self, dto: StudentDTO) -> Student:
        pass

    @abstractmethod
    def get_by_id(self, student_id: int) -> Student:
        pass

    @abstractmethod
    def list_all(self) -> List[Student]:
        pass

    @abstractmethod
    def delete(self, student_id: int) -> None:
        pass
