from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from domain.dtos.grade_dto import GradeDTO
from infra.db.models.grade import Grade

class GradeRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(self, dto: GradeDTO) -> Grade:
        grade = Grade(**dto.__dict__)
        self.db.add(grade)
        await self.db.commit()
        await self.db.refresh(grade)
        return grade

    async def get_by_id(self, id_grade: int) -> Grade:
        result = await self.db.execute(select(Grade).filter_by(id_grade=id_grade))
        return result.scalars().first()

    async def list_all(self) -> list[Grade]:
        result = await self.db.execute(select(Grade))
        return result.scalars().all()

    async def delete(self, id_grade: int) -> None:
        result = await self.db.execute(select(Grade).filter_by(id_grade=id_grade))
        entity = result.scalars().first()
        if entity:
            await self.db.delete(entity)
            await self.db.commit()
