from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from domain.dtos.subject_dto import SubjectDTO
from infra.db.models.subject import Subject

class SubjectRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(self, dto: SubjectDTO) -> Subject:
        subject = Subject(**dto.__dict__)
        self.db.add(subject)
        await self.db.commit()
        await self.db.refresh(subject)
        return subject

    async def get_by_id(self, id_subject: int) -> Subject:
        result = await self.db.execute(select(Subject).filter_by(id_subject=id_subject))
        return result.scalars().first()

    async def list_all(self) -> list[Subject]:
        result = await self.db.execute(select(Subject))
        return result.scalars().all()

    async def delete(self, id_subject: int) -> None:
        result = await self.db.execute(select(Subject).filter_by(id_subject=id_subject))
        entity = result.scalars().first()
        if entity:
            await self.db.delete(entity)
            await self.db.commit()
