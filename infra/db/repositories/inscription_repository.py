from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from domain.dtos.inscription_dto import InscriptionDTO
from infra.db.models.inscription import Inscription

class InscriptionRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(self, dto: InscriptionDTO) -> Inscription:
        inscription = Inscription(**dto.__dict__)
        self.db.add(inscription)
        await self.db.commit()
        await self.db.refresh(inscription)
        return inscription

    async def get_by_id(self, id_inscription: int) -> Inscription:
        result = await self.db.execute(select(Inscription).filter_by(id_inscription=id_inscription))
        return result.scalars().first()

    async def list_all(self) -> list[Inscription]:
        result = await self.db.execute(select(Inscription))
        return result.scalars().all()

    async def delete(self, id_inscription: int) -> None:
        result = await self.db.execute(select(Inscription).filter_by(id_inscription=id_inscription))
        entity = result.scalars().first()
        if entity:
            await self.db.delete(entity)
            await self.db.commit()
