from typing import Any, Coroutine, Sequence

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from domain.dtos.teacher_dto import TeacherDTO
from infra.db.models.teacher import Teacher
from infra.db.models.user import User

class TeacherRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(self, dto: TeacherDTO) -> Teacher:
        user = User(
            name=dto.name,
            last_name=dto.last_name,
            email=dto.email,
            password=dto.password
        )
        self.db.add(user)
        await self.db.flush()

        teacher = Teacher(
            id_user=user.id_user,
            code_employee=dto.code_employee,
            speciality=dto.speciality,
            type_contract=dto.type_contract,
            hiring_date=dto.hiring_date
        )
        self.db.add(teacher)
        await self.db.commit()
        await self.db.refresh(teacher)
        return teacher

    async def get_by_id(self, id_teacher: int) -> Teacher:
        result = await self.db.execute(select(Teacher).filter_by(id_teacher=id_teacher))
        return result.scalars().first()

    async def list_all(self) -> Sequence[Teacher]:
        result = await self.db.execute(select(Teacher))
        return result.scalars().all()

    async def delete(self, id_teacher: int) -> None:
        result = await self.db.execute(select(Teacher).filter_by(id_teacher=id_teacher))
        teacher = result.scalars().first()
        if teacher:
            await self.db.delete(teacher)
            await self.db.commit()
