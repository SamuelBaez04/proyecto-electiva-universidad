from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from domain.dtos.faculty_dto import FacultyDTO
from infra.db.models.faculty import Faculty

class FacultyRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(self, dto: FacultyDTO) -> Faculty:
        faculty = Faculty(**dto.__dict__)
        self.db.add(faculty)
        await self.db.commit()
        await self.db.refresh(faculty)
        return faculty

    async def get_by_id(self, id_faculty: int) -> Faculty:
        result = await self.db.execute(select(Faculty).filter_by(id_faculty=id_faculty))
        return result.scalars().first()

    async def list_all(self) -> list[Faculty]:
        result = await self.db.execute(select(Faculty))
        return result.scalars().all()

    async def delete(self, id_faculty: int) -> None:
        result = await self.db.execute(select(Faculty).filter_by(id_faculty=id_faculty))
        entity = result.scalars().first()
        if entity:
            await self.db.delete(entity)
            await self.db.commit()
