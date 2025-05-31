from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from domain.dtos.timetable_dto import TimetableDTO
from infra.db.models.timetable import Timetable

class TimetableRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(self, dto: TimetableDTO) -> Timetable:
        timetable = Timetable(**dto.__dict__)
        self.db.add(timetable)
        await self.db.commit()
        await self.db.refresh(timetable)
        return timetable

    async def list_all(self) -> list[Timetable]:
        result = await self.db.execute(select(Timetable))
        return result.scalars().all()

    async def delete(self, id_timetable: int) -> None:
        result = await self.db.execute(select(Timetable).filter_by(id_timetable=id_timetable))
        entity = result.scalars().first()
        if entity:
            await self.db.delete(entity)
            await self.db.commit()
